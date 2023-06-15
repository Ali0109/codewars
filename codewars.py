def fizz_buzz_func(fizz_buzz_list: list, number) -> str:
    result = ""
    for dicts in fizz_buzz_list:
        for key, value in dicts.items():
            if number % value == 0:
                result += key
    return result


fizz_buzz_list_example = [
    {"fizz": 2},
    {"buzz": 3},
    {"duzz": 5},
    {"fuzz": 7},
    {"hazz": 13},
    {"zazz": 19},
]

print(fizz_buzz_func(fizz_buzz_list_example, 38))
