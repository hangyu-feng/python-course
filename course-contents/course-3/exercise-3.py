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


def isPowerOfTwo(n):
    ''' Given an integer n, return true if it is a power of two. Otherwise, return false.
    An integer n is a power of two, if there exists an integer x such that n == 2x.
    -2**31 <= n <= 2**31
    '''
    pass


# write four classes: Animal, Bird, Eagle, Fish such that:
# each has a method getWeight() that returns it's weight
# Bird and Eagle has a method canFly() that returns True


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
