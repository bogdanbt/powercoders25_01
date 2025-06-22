# Problem: https://www.hackerrank.com/challenges/repeated-string/problem
# Score: 20

def repeated_string(s, n):
    if not s:  
        return 0
    return n // len(s) * s.count('a') + s[:n % len(s)].count('a')
