def fibo(n):
    fb = [0,1]
    for i in range(2,n+1):
        fb.append(fb[i-1] + fb[i-2])
    return fb[n]
