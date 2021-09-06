def find(l: list[int], n: int):
    """
    l is strictly increasing
    find the index of n
    if n is not in l, return -1
    """
    a = len(l)
    if a == 0 or l[0] > n or l[-1] < n:
        return -1
    up = a - 1
    low = 0
    while up >= low:
        mid = (up + low) // 2
        if l[mid] == n:
            return mid
        if l[mid] > n:
            up = mid - 1
        elif l[mid] < n:
            low = mid + 1
    return -1
        


if __name__ == "__main__":
    cases = [
        # [[1, 2, 3, 4, 5], 1, 0],
        # [[1, 2, 3, 4, 5], 5, 4],
        # [[1, 2, 3, 4, 5], 6, -1],
        # [[], 0, -1],
        # [[1,2], -1, -1],
        [[1,2,3,4,5,6,7,8,10], 9, -1]
    ]
    for l, n, result in cases:
        print(find(l, n), find(l, n) == result)
