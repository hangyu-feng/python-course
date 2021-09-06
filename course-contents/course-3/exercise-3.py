def find(l: list[int], n: int):
    """
    l is strictly increasing
    find the index of n
    if n is not in l, return -1
    """
    a = len(l)
    if a == 0:
        return -1
    b = (a - 1) // 2
    while b >= 0:
        if l[b] == n:
            return b
        if l[b] > n:
            b = b // 2
        if l[b] < n:
            b = (b + a) // 2
        if l[0] > n or l[a - 1] < n:
            return -1


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
