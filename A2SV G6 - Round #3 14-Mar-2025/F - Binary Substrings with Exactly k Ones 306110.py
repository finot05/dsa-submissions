# Problem: F - Binary Substrings with Exactly k Ones - https://codeforces.com/gym/588468/problem/F

k = int(input())
s = input()


def atmostk(k):
    count = 0
    l = 0
    ans = 0
    if k == -1:
        return 0
    for r in range(len(s)):
        
        if s[r] == '1':
            count += 1
        while count > k:
            if s[l] == '1':
                count -= 1
            l += 1
        ans += r-l+1
        
    return ans
print(atmostk(k) - atmostk(k-1))