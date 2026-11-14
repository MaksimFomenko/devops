import json

data = {
    "status": "devops-vm",
    "status": "running",
    "uptime_hours": "12"
}

with open('status.json', 'w') as f:
    json.dump(data, f, indent=2)

with open('status.json', 'r') as f:
    loaded =json.load(f)

print(loaded["status"])
print(type(loaded))