import sys

def sieve_of_eratosthenes(n):
    prime = [True] * (n + 1)
    prime[0], prime[1] = False, False
    for i in range(2, int(n ** 0.5) + 1):
        if prime[i]:
            for j in range(i * i, n + 1, i):
                prime[j] = False
    return prime

def find_prime(m, n):
    prime = sieve_of_eratosthenes(n)
    for num in range(m, n + 1):
        if prime[num]:
            print(num)
            
m, n = map(int, sys.stdin.readline().split())

find_prime(m, n)