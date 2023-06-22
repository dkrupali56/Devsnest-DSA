def solve(m, n, arr1, arr2):
    arr1 = list(filter((0).__ne__, arr1))
    arr1 = arr1 + arr2
    arr1.sort()
    return arr1
