def main():
    with open("data.txt") as f:
        lines = f.readlines()

    total = 0

    for word in lines:
        first_digit = 0
        last_digit = 0
        is_first = True
        word = replace(word)
        print(word)
        for letter in word:
            if letter.isdigit() and is_first:
                is_first = False
                first_digit = 10 * int(letter)
            if letter.isdigit():
                last_digit = int(letter)
        total += first_digit + last_digit

    print(total)


def replace(word: str) -> str:
    dict = {
        "one": "o1e",
        "two": "t2e",
        "three": "t3e",
        "four": "f4r",
        "five": "f5e",
        "six": "s6x",
        "seven": "s7n",
        "eight": "e8t",
        "nine": "n9e"
    }
    for key, value in dict.items():
        word = word.replace(key, value)

    return word


if __name__ == "__main__":
    main()
