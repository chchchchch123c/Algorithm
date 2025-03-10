import sys
n, m = map(int, sys.stdin.readline().split())
site_dict = {}
for _ in range(n):
    site, password = sys.stdin.readline().split()
    site_dict[site] = password
for _ in range(m):
    print(site_dict[sys.stdin.readline().rstrip()])