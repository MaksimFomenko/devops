import argparse
import json
import requests

parser = argparse.ArgumentParser(description="Fetch GitHub user information")
parser.add_argument("username", help="GitHub username to fetch information for")
args = parser.parse_args()

response = requests.get(f"https://api.github.com/users/{args.username}")

if response.status_code == 200:
    user_data = response.json()
    user_data = {
        "login": user_data.get("login"),
        "public_repos": user_data.get("public_repos"),
        "created_at": user_data.get("created_at")
    }
    with open(f"{args.username}.json", 'w') as f:
        json.dump(user_data, f, indent=2)

        print(f"Saved profile for {args.username} to {args.username}.json")
else:
    print(f"Error: could not fetch profile (status {response.status_code})")