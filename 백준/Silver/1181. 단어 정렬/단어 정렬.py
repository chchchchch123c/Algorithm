t = int(input())
arr = []
for i in range(t):
    arr.append(input())
arr = set(arr)
sorted_list = sorted(arr, key= lambda x : (len(x), x))
for i in sorted_list:
    print(i)