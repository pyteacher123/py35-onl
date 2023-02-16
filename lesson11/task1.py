# # Built-in (B)
# # global (G)
# def test1(): # Enclosing (E)
#     counter = 20
#     def test2(): # local (L)
#         nonlocal counter
#         counter = 30
#         print("Hello World")
#         print(counter)
#     test2()
#     print(counter)

# counter = 10
# test1()
# print(counter)

class IncorrectName(Exception):
    ...


# def validate_list(func):
#     def wrapper(*args, **kwargs):
#         for name in args[0]:
#             if not isinstance(name, str):
#                 raise IncorrectName(f"Name must be {str}")
#         return func(*args, **kwargs)
#     return wrapper


def validate_list(expect_type=str):
    def inner(func):
        def wrapper(*args, **kwargs):
            for name in args[0]:
                if not isinstance(name, expect_type):
                    raise IncorrectName(f"Name must be {expect_type}")
            return func(*args, **kwargs)
        return wrapper
    return inner


@validate_list(expect_type=str)
def get_likes_string(names):
    if len(names) == 0:
        return "no one likes this"
    elif len(names) == 1:
        return f"{names[0]} likes this"
    elif len(names) == 2:
        return f"{names[0]} and {names[1]} like this"
    elif len(names) == 3:
        return f"{names[0]}, {names[1]} and {names[2]} like this"
    else:
        return f"{names[0]}, {names[1]} and {len(names[2:])} others like this"


try:
    res = get_likes_string(["Max", "Alex"])
    print(res)
except IncorrectName as err:
    print(err)
