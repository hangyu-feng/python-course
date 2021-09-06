# question 1
def nth_digit(num: int, n: int) -> int:
    """ define a function nth_digit such that:
        nth_digit(num, n) return the nth digit of num
        if n is too large or too small, return -1
    """
    if (n != 0) and ((n < 0) or (10**n > num)):
        return -1
    else:
        return num%(10**(n+1))//(10**n)

# question 2:  convert_to_upper:  Convert the strs in the given list to uppercase.
def convert_to_upper(string_list: list[str]):
    """ Convert the strs in the given list to uppercase. """
    for i, value in enumerate(string_list):
        string_list[i] = value.upper()


# question 3
def get_x_strs(l: list[str]) -> list[str]:
    """ Given a list l, return a new list that contains only
        the elements of l that are strs that contain the
        character 'x'. Do not alter l.
    """
    newl = []
    for string in l:
        if "x" in string:
            newl.append(string)
    return newl

# question 4
def remove_vowels(s: str) -> str:
    """ Return a new str that is identical to the input str except
        that the vowels have been removed. Vowels are the letters
        a,e,i,o,u. We do not consider y a vowel.
    """
    pass


if __name__ == "__main__":
    cases = [
        [(233, 2), 2],
        [(0, 0), 0],
        [(100, 2), 1],
        [(9987, -1), -1],
        [(99, 2), -1]
    ]
    for case in cases:
        result = nth_digit(case[0][0], case[0][1])
        print(result, result == case[1])

    str1 = ["abc", "ABC"]
    convert_to_upper(str1)
    print(str1, str1 == ["ABC", "ABC"])
    str2 = ["abc", "xyz"]
    print(get_x_strs(str2), get_x_strs(str2) == ["xyz"]) 
