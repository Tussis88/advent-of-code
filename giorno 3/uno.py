import re
from rich import print

num_string = ""
num_list = []
ended = True
found = False
with open("es.txt") as f:
    lines = f.readlines()


def main():
    total = 0
    for row in range(len(lines)):
        for col in range(len(lines[0])):
            if lines[row][col].isdigit():
                check_gear(row, col)

    for num in num_list:
        print(num)
        total += int(num)

    print(total)


def checker(row: int, col: int):
    global num_string, found, ended
    symbols = ["*", "#", "-", "/", "=", "+", "@", "%", "&", "$"]

    ended = False
    num_string += lines[row][col]
    for near_row in range(-1, 2):
        new_row = row + near_row
        if new_row < 0 or new_row >= len(lines):
            continue
        else:
            for near_col in range(-1, 2):
                new_col = col + near_col
                if new_col < 0 or new_col >= len(lines[0]):
                    continue
                else:
                    if lines[new_row][new_col] in symbols:
                        found = True

    if col + 1 < len(lines[0]) and not lines[row][col + 1].isdigit():
        ended = True
        if found == True:
            num_list.append(num_string)
            found = False
        num_string = ""


def check_gear(row: int, col: int):
    global num_string, found, ended, last_symbol
    symbol = "*"

    ended = False
    num_string += lines[row][col]
    for near_row in range(-1, 2):
        new_row = row + near_row
        if new_row < 0 or new_row >= len(lines):
            continue
        else:
            for near_col in range(-1, 2):
                new_col = col + near_col
                if new_col < 0 or new_col >= len(lines[0]):
                    continue
                else:
                    if lines[new_row][new_col] == symbol:
                        found = True

    if col + 1 < len(lines[0]) and not lines[row][col + 1].isdigit():
        ended = True
        if found == True:
            num_list.append(num_string)
            found = False
        num_string = ""


if __name__ == "__main__":
    main()
