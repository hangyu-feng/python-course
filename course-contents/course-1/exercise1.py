# question 1
def nth_digit(num: int, n: int) -> int:
    """ define a function nth_digit such that:
        nth_digit(num, n) return the nth digit of num
        if n is too large or too small, return -1
    """
    if (n < 0) or (10**n > num):
        return -1
    else:
        return num%(10**n)//(10**n)

# question 2:  convert_to_upper:  Convert the strs in the given list to uppercase.
def convert_to_upper(string_list: list[str]):
    """ Convert the strs in the given list to uppercase. """
    pass


# question 3
def get_x_strs(l: list[str]) -> list[str]:
    """ Given a list l, return a new list that contains only
        the elements of l that are strs that contain the
        character 'x'. Do not alter l.
    """
    pass


if __name__ == "__main__":
    result = nth_digit(15, 1)
    print(result, result == 1)
