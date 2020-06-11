# ex 1
def dict_from_lists(key_list: list, values_list: list) -> dict:
    if not isinstance(values_list, list) or not isinstance(values_list, list):
        print("Invalid value of one of the input arguments. Expected list type parameters.")
        quit()
    else:
        return dict(zip(key_list, values_list))


# ex 2
def merge_dictionaries(dict1: dict, dict2: dict) -> dict:
    if not isinstance(dict1, dict) or not isinstance(dict2, dict):
        print("Invalid value of one of the input arguments. Expected list type parameters.")
        quit()
    return {**dict1, **dict2}


# ex 5
def extract_dict(dictionary: dict, *args: any) -> dict:
    if not isinstance(dictionary, dict):
        print("Invalid value type. Expected dict type parameter.")
        quit()
    else:
        tmp_dict = dict()
        for i in args:
            if i in dictionary.keys():
                tmp_dict[i] = dictionary[i]
        return tmp_dict


# ex 6
def remove_from_dict(dictionary: dict, keys_list: list) -> dict:
    if not isinstance(dictionary, dict):
        print("Invalid value type. Expected dict type parameter.")
        quit()
    elif not isinstance(keys_list, list):
        print("Invalid value type. Expected list type parameter.")
        quit()
    else:
        for i in keys_list:
            if i in dictionary.keys():
                dictionary.pop(i)
    return dictionary


# ex 7
def check_if_key_exist(dictionary: dict, value: any) -> bool:
    if not isinstance(dictionary, dict):
        print("Invalid value type. Expected dict type parameter.")
        quit()
    else:
        if value in dictionary.values():
            return True
        else:
            return False


# ex 8
def rename_key_in_dict(dictionary: dict, old_key: any, new_key: any) -> dict:
    if not isinstance(dictionary, dict):
        print("Invalid value type. Expected dict type parameter.")
        quit()
    elif old_key not in dictionary.keys():
        print("Given value does not exist in dictionary.")
        quit()
    else:
        dictionary[new_key] = dictionary[old_key]
        return dictionary


# ex 9
def get_key_with_min_value(dictionary: dict) -> dict:
    if not isinstance(dictionary, dict):
        print("Invalid value type. Expected dict type parameter.")
        quit()
    else:
        min_dict_val = min(dictionary.values())
        return list(dictionary.keys())[list(dictionary.values()).index(min_dict_val)]
