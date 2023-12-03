from rich import print

with open("data.txt") as f:
    lines = f.readlines()

unique_symbols = set()

for line in lines:
    for char in line:
        if not char.isdigit():
            unique_symbols.add(char)

print(unique_symbols)
