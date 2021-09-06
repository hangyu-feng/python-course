# time complexity
# big-O: worst case scenario

def f(l: list[int]):
    """ find O(n), n is size of l """
    size = len(l)
    for i in range(size):
        a = l[i:]

def g(num: int, l: list[int]):
    """ find O(n), n is size of l """
    for item in l:
        if num == item:
            return True
    return False

def h(l: list[int]):
    """ find O(n), n is size of l """
    n = len(l)
    while n >= 0:
        a = l[n]
        n = n // 2


# recurssion

def fib(n):
    """ 1, 1, 2, 3, 5, 8, ...
    fib(0) = fib(1) = 1
    fib(2) = 2
    """
    if n == 0 or n == 1:
        return 1
    return fib(n-1) + fib(n-2)

def fib(n):
    """ dynamic programming """
    a, b = 1, 1
    for _ in range(n):
        a, b = a + b, a
    return b

def find(l: list[int], n: int):
    """
    l is strictly increasing
    find the index of n
    if n is not in l, return -1

    see exercise-3
    """
    if not l:
        return -1
    m = len(l) // 2
    if l[m] == n:
        return m
    if l[m] > n:
        return find(l[:m], n)
    right = find(l[m+1:], n)
    if right == -1:
        return -1
    return m + right + 1

if __name__ == "__main__":
    cases = [
        [[1, 2, 3, 4, 5], 1, 0],
        [[1, 2, 3, 4, 5], 5, 4],
        [[1, 2, 3, 4, 5], 6, -1],
        [[], 0, -1],
        [[1,2], -1, -1],
        [[1,2,3,4,5,6,7,8,10], 9, -1]
    ]
    for l, n, result in cases:
        print(find(l, n), find(l, n) == result)
