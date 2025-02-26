from collections import deque
t = int(input())
for i in range(t):
    n, m = map(int, input().split())
    documents = list(map(int, input().split()))
    queue = deque([(documents, idx) for idx, documents in enumerate(documents)])
    order = 0
    while queue:
        cur = queue.popleft()
        if any(cur[0] < other[0] for other in queue):
            queue.append(cur)
        else:
            order += 1
            if cur[1] == m:
                print(order)
                break