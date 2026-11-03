#!/usr/bin/env python3
import requests
import sys
import json
import argparse
import socket

def check_status(url, expected_status):
    try:
        response = requests.get(url, timeout=5)
        ok = response.status_code == expected_status

        if ok:
            detail = f"OK (status {response.status_code})"
        else:
            detail = f"FAIL (status {response.status_code})"
        return ok, detail
    
    except requests.RequestException:
        return False, "FAIL (Failed to connect)"


def check_tcp(site):
    try:
        with socket.create_connection((site['host'], site['port']), timeout=5):
            return True, "OK (TCP connection successful)"
    except (socket.timeout, socket.error):
        return False, "FAIL (TCP connection failed)"



def main():
    parser = argparse.ArgumentParser(description="Simple health checker")
    parser.add_argument("config", help="path to JSON file with checks")
    args = parser.parse_args()

    try:
        with open(args.config) as file:
            sites = json.load(file)
        
    except FileNotFoundError:
        print(f"Error: file '{args.config}' not found", file=sys.stderr)
        sys.exit(2)
    except json.JSONDecodeError:
        print(f"Error: file '{args.config}' is not a valid JSON", file=sys.stderr)
        sys.exit(2)
    
    fail_try = 0
    total_try = len(sites)
    
    for site in sites:
        if site['type'] == 'http':
            status_ok, detail = check_status(site['url'], site['expected_status'])
        elif site['type'] == 'tcp':
            status_ok, detail = check_tcp(site)
        else:
            status_ok, detail = False, "FAIL (unknown type)"

        print(f"{site['name']} -> {detail}")
        if not status_ok:
            fail_try += 1

    print(f"Failed: {fail_try} of {total_try}")

    sys.exit(1 if fail_try > 0 else 0)


if __name__ == "__main__":
    main()