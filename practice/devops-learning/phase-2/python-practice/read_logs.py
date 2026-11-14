with open("logs.txt", "r") as f:
    for i, line in enumerate(f, start=1):
        print(f"{i}: {line.strip()}")
