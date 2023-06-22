from math import gcd
from functools import reduce

def gcd(a,b):

    if b==0:
        return a

    return gcd(b,a%b)


def solve(n, deck):
    
    hashmap={}

    for i in deck:

        if i in hashmap:
            hashmap[i]+=1

        else:
            hashmap[i]=1
    x=reduce(gcd,hashmap.values())
    if x==1:
        return 0

    return 1
