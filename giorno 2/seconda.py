# 12 red, 13 green, and 14 blue
import re
from rich import print


def main():
    pattern = re.compile(r"\b(\d+)\s*(red|blue|green)\b")
    games = []
    counter = 0
    total = 0
    with open("data.txt") as f:
        lines = f.readlines()
    for line in lines:
        min_red = 1
        min_green = 1
        min_blue = 1
        counter += 1
        sets = line.split(";")
        set_list = []
        for set in sets:
            game_list = []
            set_list.append(pattern.findall(set))
            for set in set_list:
                for value, color in set:
                    if color == "red" and int(value) > min_red:
                        min_red = int(value)
                    if color == "green" and int(value) > min_green:
                        min_green = int(value)
                    if color == "blue" and int(value) > min_blue:
                        min_blue = int(value)

                game_list.append({"red": min_red, "green": min_green, "blue": min_blue})
        total += min_red * min_green * min_blue
        games.append(game_list)
    print(games)
    print(total)


if __name__ == "__main__":
    main()
