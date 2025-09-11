def f(x):
    if x == 7:
        warning = "f(7) is illegal"
        print(warning)
        return warning
    return (x + 3) * 2


def g(x, y):
    if not isinstance(x, int):
        report = "x must be an int in g(x,y)"
        return report
    else:
        try:
            # Be aware:
            # you can use `+` with two strings
            # you can use `+` with two numbers
            # you can't use `+` with an integer and a string.
            # Doing so gives an error.
            return x + f(y)
        except:
            return 42


def h(x, y):
    return g(x, y - 3)


def main():
    list_of_args = [(1, 2), ("hello", 4), (3, 10), (4, 3)]

    # This will loop over the list `list_of_args`.
    # The first pass, `args` will become the first entry in the list,
    # which is the tuple (1, 2). The second pass, `args` will become
    # the tuple `("hello", 4)`.
    for args in list_of_args:
        i = args[0]
        j = args[1]
        print(f"i = {i}, j = {j}")
        print(str(h(i, j)))


if __name__ == "__main__":
    main()
