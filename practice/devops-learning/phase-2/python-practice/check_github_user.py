import argparse
import requests

parser = argparse.ArgumentParser(description="Check a GitHub user`s public information")
parser.add_argument("username", help="GitHub username to look up")
args = parser.parse_args()

response = requests.get(f"https://api.github.com/users/{args.username}")

if response.status_code == 200:
    data = response.json()
    print(f"User: {data['login']}")
    print(f"Public Repositories: {data['public_repos']}")
    print(f"Created At: {data['created_at']}")
else:
    print(f"Error: user not found (status {response.status_code})")