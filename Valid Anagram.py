def solve(s1, s2):
    xor = 0
    if len(s2)!=len(s1):
        return 0
    for i in range(len(s1)):
        xor^=ord(s1[i])
        xor^=ord(s2[i])
    return 1 if not(xor) else 0
