def sport_plan_performance(plan, k, lower, upper):
    ss = [0] + plan

    for i in range(1, len(ss)):
        ss[i] = ss[i-1] + ss[i]
    
    ans, n = 0, len(plan)
    print(ss)
    for i in range(n - k+1):
        t = ss[i+k] - ss[i]
        if t < lower:
            ans -= 1
        elif t > upper:
            ans += 1
            
    return ans

b = sport_plan_performance(plan = [1,2,3,4,5], k = 1, lower = 3, upper = 3)
print(b)