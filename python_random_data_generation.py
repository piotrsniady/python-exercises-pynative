import random
import string
import secrets
import datetime
import time


# ex 1
def num_gen() -> list:
    gen_num = []
    while len(gen_num) <= 2:
        generated_number = random.randint(100, 999)
        if generated_number % 5 == 0:
            gen_num.append(generated_number)
    return gen_num


# ex 2
def lottery_tickets_generator() -> list:
    lottery_tickets = []
    for ticket in range(100):
        lottery_tickets.append(random.randrange(1000000000, 9999999999))

    winner_tickets = random.sample(lottery_tickets, 2)
    return winner_tickets


# ex 3
def generate_otp() -> str:
    otp = ""
    for i in range(6):
        otp += str(random.randint(1, 9))
    return otp


# ex 4
def random_char_from_string(string_val: str) -> str:
    letters = [char for char in string_val]
    return ''.join(random.choices(letters, k=1))


# ex 5
def generate_random_string() -> str:
    return ''.join(random.choice(string.ascii_letters) for _ in range(5))


# ex 6
def generate_random_password(password_len: int) -> str:
    upper_letters = "ABCDEFGHIJKLMNOPRSTUVWXYZ"
    lower_letters = upper_letters.lower()
    numbers = "1234567890"
    special_symbols = "!@#$%^&*()+_?"

    full_password_options = [upper_letters + lower_letters + numbers + special_symbols]
    base_password_options = [upper_letters, numbers, special_symbols]

    base_password = [random.choice(i) for _ in range(2) for i in base_password_options]
    extend_password = [random.choice(i) for _ in range(password_len - len(base_password)) for i in full_password_options]

    password = base_password + extend_password
    return "".join(password)


# ex 7
def rand_num_multiplication() -> float:
    first_float = random.uniform(0.1, 1.0)
    second_float = random.uniform(9.5, 99.5)
    return first_float * second_float


# ex 8
def generate_bytes_and_url() -> (str, str):
    token = secrets.token_hex(nbytes=64)
    url = secrets.token_urlsafe(nbytes=64)
    return token, url


# ex 9
def roll_dice_same_number() -> int:
    random.seed(0)
    dice_numbers = [1, 2, 3, 4, 5, 6]
    num = random.choice(dice_numbers)
    return num
