import string
import random

lowercase_alphabet = string.ascii_lowercase

dicts_list = [{} for _ in range(random.randint(2, 11))]


for x in dicts_list:
    for _ in range(random.randint(1, len(lowercase_alphabet))):
        x.setdefault(random.choice(lowercase_alphabet), random.randint(0, 101))

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

print(single_dict)
