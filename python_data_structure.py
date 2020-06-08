# ex 1
def odd_even_list_index(list_1: list, list_2: list) -> list:
    return list_1[1::2] + list_2[0::2]


# ex 2
def remove_at_4(num_list: list) -> None:
    fourth_index = [num for index, num in enumerate(num_list) if index == 4]
    num_list.remove(fourth_index[0])
    num_list.insert(2, fourth_index[0])
    print(num_list)
    num_list.insert(len(num_list), fourth_index[0])
    print(num_list)
    return None


# ex 3
def equal_chunks(num_list: list) -> list:
    set_array = [num_list[x:x + 3] for x in range(0, len(num_list), 3)]
    for i_set in set_array:
        if len(i_set) != 3:
            print("[WARNING] Some elements of list are different from 3 element subsample.")
    return set_array


# ex 4
def list_to_dict(num_list: list) -> dict:
    num_dict = dict()
    for item in num_list:
        if item in num_dict:
            num_dict[item] += 1
        else:
            num_dict[item] = 1
    return num_dict


# ex 5
def pair_two_list(first_list: list, second_list: list) -> list:
    if len(first_list) != len(second_list):
        print("Given lists are not equal.")
        quit()
    else:
        return list(map(lambda x, y: (x, y),first_list, second_list))


# ex 6
def set_diff_and_intersection(set_1: set, set_2: set) -> str:
    set_intersection = set(set_1).intersection(set(set_2))
    set_diff = set(set_1).difference(set(set_2))
    return f"Intersection is {set_intersection}, first Set after removing common elements {set_diff}."


# ex 7
def subsets(set_1: set, set_2: set) -> None:
    first_is_subset = set_1.issubset(set_2)
    second_is_subset = set_2.issubset(set_1)
    print(f"First set is subset of second set - {first_is_subset}.")
    print(f"Second set is subset of First set - {second_is_subset}.")

    first_is_superset = set_1.issuperset(set_2)
    second_is_superset = set_2.issuperset(set_1)
    print(f"First set is superset of second set - {first_is_superset}.")
    print(f"Second set is superset of First set - {second_is_superset}.")

    if first_is_subset:
        print(set(set_1).difference(set(set_2)))
        print(set(set_2))
    else:
        print(set(set_2).difference(set(set_1)))
        print(set(set_1))
    return None


# ex 8
def not_in_list_in_dict(num_list: list, dictionary: dict) -> list:
    list_set = set(num_list)
    dict_set = set()

    for key, value in dictionary.items():
        dict_set.add(value)

    for i in list_set.difference(dict_set):
        if i in num_list:
            num_list.remove(i)
    return num_list


# ex 9
def dictionary_values_to_list(dictionary: dict) -> list:
    num_set = set()
    [num_set.add(value) for key, value in dictionary.items()]
    return list(num_set)


# ex 10
def min_max_in_tuple_list(num_list: list) -> str:
    tuple_list = tuple(set(num_list))
    min_tuple_list = min(tuple_list)
    max_tuple_list = max(tuple_list)
    return f"Tuple list: {tuple_list}, min tuple list: {min_tuple_list}, max tuple list: {max_tuple_list}"
