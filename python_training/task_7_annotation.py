# a: int = 5
# b: str = "string"
# c: list = [1, 2]
#
# def indent(s: str, width: int) -> str:
#     return " " * (max(0, width - len(s))) + s
#
# print(indent("69", 69))

# def func(s: str = "") -> int:
#     return(len(s))
#
# print(func())
#
# def min_list(a: list, b: list) -> int:
#     return(max(len(a), len(b)))
#
# print(min_list(a=(6, 2, 5), b=(3, 4)))

# def func_3(a: list) -> list:
#     a.append("test")
#     return a
#
# print(func_3(["one", 2, 3]))

def func_4(a:list) -> int:
    result = 0
    for elem in a:
        result = result + elem
    return result

print(func_4([1, 4, 6]))

