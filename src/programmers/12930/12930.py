# problem source: https://school.programmers.co.kr/learn/courses/30/lessons/12930

def solution(s):
    ans = ""
    ss = s.split()
    for s in ss:
        for i in range(len(s)):
            if i & 1 == 0:
                ans += s[i].upper()
            else:
                ans += s[i]
        ans += ' '
    
    return ans[:-1]
