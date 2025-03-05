import sys
n, m = map(int, sys.stdin.readline().split())
id_dict = {}
name_dict = {}
for i in range(1, n + 1):
    pokemon = sys.stdin.readline().rstrip()
    id_dict[i] = pokemon
    name_dict[pokemon] = i
for _ in range(m):
    x = input()
    if x.isdigit():
        print(id_dict[int(x)])
    else:
        print(name_dict[x])