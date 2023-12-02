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
        valid_checker = True
        counter += 1
        sets = line.split(";")
        set_list = []
        for set in sets:
            game_list = []
            # game_list.clear()
            set_list.append(pattern.findall(set))
            for set in set_list:
                colors_list = []
                # colors_list.clear()
                for value, color in set:
                    colors_list.append({color: value})
                    if color == "red" and int(value) > 12:
                        valid_checker = False
                    if color == "green" and int(value) > 13:
                        valid_checker = False
                    if color == "blue" and int(value) > 14:
                        valid_checker = False

                game_list.append(colors_list)

        if valid_checker:
            total += counter
        games.append(game_list)
    print(total)


if __name__ == "__main__":
    main()
