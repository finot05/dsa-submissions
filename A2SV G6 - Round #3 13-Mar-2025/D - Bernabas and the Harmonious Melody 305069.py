# Problem: D - Bernabas and the Harmonious Melody - https://codeforces.com/gym/588468/problem/D

def is_palindrome(l, r, char, s):
    count = 1
    while l<r:
        if s[l] != s[r]:
            if s[l] == char:
                count += 1
                l += 1
            elif s[r] == char:
                count += 1
                r -= 1
            else:
                return False, 0
        else:
            l += 1
            r -= 1
    return True, count

def min_removals_to_palindrome(n, s):
    if s == s[::-1]:
        return 0
    l, r = 0, n-1
    min_count = float('inf')
    while l<r:
        if s[l] != s[r]:
            valid1, count1 =  is_palindrome(l+1, r, s[l], s) 
            valid2, count2 = is_palindrome(l, r-1, s[r], s)
            if valid1:
                min_count = min(min_count, count1)
            if valid2:
                min_count = min(min_count, count2)
            
            return min_count if min_count != float('inf') else -1
        
        l += 1
        r -= 1
    return 0

t = int(input())
results = []

for _ in range(t):
    n = int(input())
    s = input().strip()
    result = min_removals_to_palindrome(n, s)
    results.append(result)

for res in results:
    print(res)
