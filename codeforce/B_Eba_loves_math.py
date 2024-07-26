for _ in range(int(input())):
	n = int(input())
	arr = list(map(int,input().split()))
	x = arr[0]
	for i in range(n):
		x &= arr[i]
	print(x)
