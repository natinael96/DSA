chars = input()

maxLen = 1
currLen = 1

for r in range(1, len(chars)):
            
    if chars[r] == chars[r-1]:
        currLen += 1
    else:
        currLen = 1
    maxLen = max(currLen, maxLen)
print(maxLen)
