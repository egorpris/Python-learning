import string
import random


def generate_keys(func):
    def wrapper(min, max):
        dicts_list = func(min, max)
        lowercase_alphabet = string.ascii_lowercase
        for x in dicts_list:
            for _ in range(random.randint(1, len(lowercase_alphabet))):
                x.setdefault(random.choice(lowercase_alphabet), random.randint(0, 101))
        return dicts_list

    return wrapper


@generate_keys
def generate_dicts(min, max):
    return [{} for _ in range(random.randint(min, max+1))]


def merge_dicts(dicts_list):
    single_dict = {}
    for l, i in enumerate(dicts_list):
        for key in i:
            is_unique = True
            for y in dicts_list:
                if y != i and key in y:
                    is_unique = False
                    break

            if is_unique:
                single_dict.setdefault(key, i[key])
                continue

            is_max = True
            for y in dicts_list:
                if y != i and key in y:
                    if i[key] < y[key]:
                        is_max = False
                        break

            if is_max:
                single_dict.setdefault(key + '_' + str(dicts_list.index(i)), i[key])

    return single_dict


dicts_list = generate_dicts(2, 11)
single_dict = merge_dicts(dicts_list)
print(single_dict)
