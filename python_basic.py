from typing import List


# ex 1
def two_numbers(num1: int, num2: int) -> int:
    if not isinstance(num1, int):
        print(f"{num1} is not a digit.")
        quit()
    elif not isinstance(num2, int):
        print(f"{num2} is not a digit.")
        quit()
    else:
        num_1, num_2 = int(num1), int(num2)
        if int(num_1) * int(num_2) >= 1000:
            return num_1 + num_2
        else:
            return num_1 * num_2


# ex 3
def even_index_string(string: str) -> str:
    for index, char in enumerate(string):
        if index % 2 == 0:
            return f"index[ {index} ] {char}"


# ex 4
def remove_char(string: str, n: int) -> str:
    if n + 1 not in range(len(string) + 1):
        print("Given number is out of string range.")
        quit()
    else:
        return string[n:]


# ex 5
def same_end_and_start(num_list: list) -> List[bool]:
    return [True if num_list[0] == num_list[-1] else False]


# ex 6
def divisible_by_5(num_list: list) -> list:
    results = []
    for num in num_list:
        if num % 5 == 0:
            results.append(num)
    return results


# ex 7
def emma_word_count(string: str, word: str) -> str:
    count = 0
    for char in string.split():
        if char == word:
            count += 1
    return f"{word} appeared {count} times."


# ex 8
def print_pattern():
    for i in range(1, 6):
        for j in range(i):
            print(f"{i}", end=" ")
        print()


# ex 9
def reverse_number(number: int) -> bool:
    if not isinstance(number, int):
        print("Given value is not a number.")
        quit()
    else:
        return str(number) == str(number)[::-1]


# ex 10
def concat_lists(num_list_1: list, num_list_2: list) -> list:
    if not isinstance(num_list_1, list) or not isinstance(num_list_2, list):
        print("One or all arguments are not list type.")
        quit()
    else:
        list_one_odd = [odd for odd in num_list_1 if odd % 2 != 0]
        list_two_even = [even for even in num_list_2 if even % 2 == 0]
        return list_one_odd + list_two_even
