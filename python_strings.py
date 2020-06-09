from collections import Counter


# ex 1
def middle_three_chars(string: str) -> str:
    if not isinstance(string, str):
        print("Given value must be a string type.")
        quit()
    elif len(string) < 7:
        print("You entered too short string. Required string with 7 characters.")
        quit()
    elif len(string) % 2 == 0:
        print("You entered a string with even number of characters. Required odd number of characters.")
        quit()
    else:
        middle_char = int(len(string) / 2)
        return string[middle_char - 1: middle_char + 2]


# ex 2
def append_middle(s1: str, s2: str) -> str:
    if not isinstance(s1, str) or not isinstance(s2, str):
        print("One or all of the arguments are not string type.")
        quit()
    else:
        if len(s1) % 2 == 0:
            return s1[:2] + s2 + s1[2:]
        else:
            return s1[:round(int(len(s1)) / 2)] + s2 + s1[round(int(len(s1)) / 2):]


# ex 3
def mix_string(s1: str, s2: str) -> str:
    if not isinstance(s1, str) or not isinstance(s2, str):
        print("One or all of the arguments are not string type.")
        quit()
    else:
        strings = [s1, s2]
        first_chars, middle_chars, last_chars = [], [], []
        for string in strings:
            first_char = string[0]
            if len(string) % 2 != 0:
                middle_char = string[int(len(string) / 2)]
            else:
                middle_char = string[round(int(len(string)) / 2 - 1)]
            last_char = string[-1]

            first_chars.append(first_char)
            middle_chars.append(middle_char)
            last_chars.append(last_char)
        return "".join(first_chars + middle_chars + last_chars)


# ex 4
def arrange_string(string: str) -> str:
    lower_chars = []
    upper_chars = []

    for char in string:
        if char.islower():
            lower_chars.append(char)
        else:
            upper_chars.append(char)
    return "".join(sorted(lower_chars, reverse=False)) + "".join(sorted(upper_chars, reverse=False))


# ex 5
def count_characters(string: str) -> str:
    symbols_dictionary = {"letter": 0, "digit": 0, "symbol": 0}

    for char in string:
        if char.islower():
            symbols_dictionary["letter"] += 1
        if char.isupper():
            symbols_dictionary["letter"] += 1
        if char.isdigit():
            symbols_dictionary["digit"] += 1
        if char in "#!@$%^&*()":
            symbols_dictionary["symbol"] += 1
    return f"Total counts of chars, digits and symbols: Chars = {symbols_dictionary['letter']}, Digits = {symbols_dictionary['digit']}," \
        f" Symbol = {symbols_dictionary['symbol']}."


# ex 6
def alternately_characters(s1: str, s2: str) -> str:
    if len(s1) == len(s2):
        long_word = s1
        short_word = s2
    elif len(s1) > len(s2):
        long_word = s1
        short_word = s2
    else:
        long_word = s2
        short_word = s1

    reversed_word = short_word[::-1]
    rest_of_longer_word = long_word[len(reversed_word):]
    concatenation = "".join(list(map(lambda x, y: x + y, long_word, reversed_word)))
    return concatenation + rest_of_longer_word


# ex 7
def string_character_balance(s1: str, s2: str) -> bool:
    return [True if s2 in s1 else False][0]


# ex 8
def find_usa(string: str) -> int:
    count = 0
    for char in string.lower().split():
        if char == "usa":
            count += 1
    return count


# ex 9
def sum_and_average_of_digits(string: str) -> (int, int):
    digits = []
    [digits.append(char) for char in string.split() if char.isdigit()]
    digits_sum = sum(map(int, "".join(digits)))
    digits_avg = sum(map(int, "".join(digits))) / len("".join(digits))
    return digits_sum, digits_avg


# ex 10
def count_chars(string: str) -> dict:
    return Counter(string)
