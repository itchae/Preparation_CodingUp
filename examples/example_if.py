def if_example(a, b):
    if b > a:
        print("b is greater than a")
    elif a == b:
        print("a and b are equal")
    else:
        print("a is greater than b")


def if_example_2(a, b):
    print("A") if a > b else print("=") if a == b else print("B")
