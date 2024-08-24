s = input()
k = int(input())

st = set()

for i in s:
    if i not in st:
        st.add(i)

if len(s) < k:
    print('impossible')
else:
    print(max(k - len(st), 0))
    
