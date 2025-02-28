import sys

def max_len(k, n, arr):
    start, end = 1, max(arr)
    answer = 0
    
    while start <= end:
        mid = (start + end) // 2
        count = sum(i // mid for i in arr)
        
        if count >= n:
            answer = mid
            start = mid + 1
        else:
            end = mid - 1
    return answer

k, n = map(int, sys.stdin.readline().split())
arr = []
for i in range(k):
    arr.append(int(sys.stdin.readline().strip()))
print(max_len(k, n, arr))