# Problem: Almost Prime - https://codeforces.com/problemset/problem/26/A

n = int(input())

def is_almost_prime(n):
    count = 0
    for x in range(2, n + 1):
        factors = set()
        d = 2
        temp = x
        while d * d <= temp:
            if temp % d == 0:
                factors.add(d)
                while temp % d == 0:
                    temp //= d
            d += 1
        if temp > 1:
            factors.add(temp)
        if len(factors) == 2:
            count += 1
    return count

print(is_almost_prime(n))
