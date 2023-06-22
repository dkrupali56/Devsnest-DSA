import heapq

def solve(matrix, k): m = {} for i in range(len(matrix)): m[i] = matrix[i].count(1)

minHeap = []
for row, num in m.items():
    heapq.heappush(minHeap, (num, row))
    
res = [heapq.heappop(minHeap)[1] for j in range(k)]
return res
