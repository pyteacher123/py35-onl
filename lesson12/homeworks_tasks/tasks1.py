"""
Algorithm:
first_dict = { 'a': 1, 'b': 2, 'c': 3}
second_dict = { 'c': 3, 'd': 4,'e': 5}
"""

first_dict = {'a': 1, 'b': 2, 'c': 3, 'k': 5}
second_dict = {'c': 3, 'd': 4, 'e': 5, 'k': 10}


def merge_dicts(first_dict, second_dict):
    merged_dict = {}
    first_dict_keys = set(first_dict.keys())
    second_dict_keys = set(second_dict.keys())
    for key in first_dict_keys.union(second_dict_keys):
        merged_dict[key] = [first_dict.get(key), second_dict.get(key)]
    return merged_dict


if __name__ == "__main__":
    res = merge_dicts(first_dict, second_dict)
    print(res)
