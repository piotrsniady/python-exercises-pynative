# ex 1
def name_and_age(name: str, age: int) -> str:
    if not isinstance(name, str):
        print("Wrong type of value. Expected string type value.")
        quit()
    elif not isinstance(age, int):
        print("Wrong type of value. Expected int type value.")
        quit()
    else:
        return f"{name}, {age}."


# ex 2
def func1(*args: int) -> None:
    for i in args:
        if not isinstance(i, int):
            print("Not all values ares integer type.")
            quit()
        else:
            print(i)


# ex 3
def calculation(a: int, b: int) -> (int, int):
    if not isinstance(a, int):
        print("Wrong type of value. Expected integer type value.")
        quit()
    elif not isinstance(a, int):
        print("Wrong type of value. Expected integer type value.")
        quit()
    else:
        addition = a + b
        subtraction = a - b
        return addition, subtraction


# ex 4
def show_employee(name: str, salary: int = None) -> (str, int):
    if not isinstance(name, str):
        print("Wrong type of value. Expected string type value.")
        quit()
    elif not isinstance(salary, int):
        print("Wrong type of value. Expected integer type value.")
        quit()
    else:
        if salary is None:
            salary = 9000
            return name, salary
        else:
            return name, salary


# ex 6
def recursive_sum(n: int = 10) -> int:
    if not isinstance(n, int):
        print("Wrong type of value. Expected integer type value.")
        quit()
    else:
        if n <= 1:
            return n
        else:
            return n + recursive_sum(n - 1)


# ex 8
def gen_nums_list(min_val: int, max_val: int) -> list:
    if not isinstance(min_val, int):
        print("Wrong type of value. Expected integer type value.")
        quit()
    elif not isinstance(max_val, int):
        print("Wrong type of value. Expected integer type value.")
        quit()
    else:
        even_nums = []
        for num in range(min_val, max_val + 1):
            if num % 2 == 0:
                even_nums.append(num)
        return even_nums


# ex 9
def return_largest(num_li: list) -> int:
    if not isinstance(num_li, list):
        print("Wrong type of value. Expected list type value.")
        quit()
    else:
        return max(num_li)
