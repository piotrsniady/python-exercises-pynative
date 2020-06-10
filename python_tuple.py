# ex 1
def reverse_tuple(tup: tuple) -> tuple:
    if not isinstance(tup, tuple):
        print("Wrong type of input. Expected tuple.")
        quit()
    elif len(tup) < 2:
        print("Given tuple has length lower than 2.")
        quit()
    else:
        return tup[::-1]


# ex 2
def access_value_in_tuple(tup: tuple, value: any) -> int:
    if not isinstance(tup, tuple):
        print("Wrong type of input. Expected tuple.")
        quit()
    elif len(tup) < 0:
        print("Wrong length of tuple.")
        quit()
    else:
        return [i for tup_elem in tup for i in tup_elem if i == value][0]


# ex 4
def swap_tuples(tup1: tuple, tup2: tuple) -> (tuple, tuple):
    if not isinstance(tup1, tuple) or not isinstance(tup2, tuple):
        print("Wrong type of one of the input tuple.")
        quit()
    else:
        tup1, tup2 = tup2, tup1
        return tup1, tup2


# ex 6
def get_values_from_tuple(tup: tuple, val1: int, val2: int) -> (int, int):
    if not isinstance(tup, tuple):
        print("Wrong type of input. Expected tuple.")
        quit()
    elif not isinstance(val1, int) or not isinstance(val2, int):
        print("Wrong type of one of the input value.")
        quit()
    else:
        if val1 not in tup:
            print(val1)
        elif val2 not in tup:
            print(val2)
        else:
            return val1, val2


# ex7
def add_to_tuple_value(tup: tuple) -> str:
    if not isinstance(tup, tuple):
        print("Wrong type of input. Expected tuple.")
        quit()
    else:
        for i in tup:
            if isinstance(i, list):
                return str(i[0]) + str(i[0])[:1]


# ex 8
def sort_tuples(tup) -> list:
    if not isinstance(tup, tuple):
        print("Wrong type of input. Expected tuple.")
        quit()
    else:
        tup_li = [sub_tuple for sub_tuple in tup]
        tup_li.sort(key=lambda x: x[1])
        return tup_li


# ex 9
def count_values_in_tuple(tup: tuple, value: int) -> int:
    if not isinstance(tup, tuple):
        print("Wrong type of input value. Expected tuple.")
        quit()
    elif not isinstance(value, int):
        print("Wrong type of input value. Expected int.")
        quit()
    elif value not in tup:
        print("Given value is not in tuple.")
        quit()
    else:
        value_count = 0
        for num in tup:
            if num == value:
                value_count += 1
        return value_count


# ex 10
def check_if_all_the_same(tup: tuple) -> bool:
    if not isinstance(tup, tuple):
        print("Wrong type of input value. Expected tuple.")
        quit()
    elif len(tup) <= 0:
        print("Empty tuple value.")
        quit()
    else:
        iterator = iter(tup)
        try:
            first = next(iterator)
        except StopIteration:
            return True
        return all(first == rest for rest in iterator)
