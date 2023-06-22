from heapq import *
def solve(matrix, k):
    n = len(matrix)
    heap=[]
    for i in range(n*n):
        row = i // n
        col = i % n
        if k>0:
            heappush(heap,-1*matrix[row][col])
            k-=1
        else:
            if -1*heap[0] > matrix[row][col]:
                heappushpop(heap,-1*matrix[row][col])
    
    return -1 * heap[0]
