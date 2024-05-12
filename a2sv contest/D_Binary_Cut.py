t = int(input())

for _ in range(t):
    s = input()
    
    cnt = 1
    flag = False
    if sorted(s) == list(s):
        cnt = 1
    else:
        for i in range(1, len(s)):
            if s[i] !=  s[i-1]:
                if s[i - 1] == '0' and s[i] == "1" and not flag:
                    flag = True
                    cnt -= 1
                cnt += 1
    print(cnt)
