def LCS(str1, str2, n, m):
    dp = [[0]*(n+1) for _ in range(m+1)]
    
    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif str1[j - 1] == str2[i - 1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i][j-1], dp[i-1][j])
    return dp[m][n]

# Test Case 1
str1 = "ABCD"
str2 = "ACDF"
n = len(str1)
m = len(str2)
print(LCS(str1, str2, n, m))  # Output should be 3, as "ACD" is the longest common subsequence.

# Test Case 2
str1 = "AGGTAB"
str2 = "GXTXAYB"
n = len(str1)
m = len(str2)
print(LCS(str1, str2, n, m))  # Output should be 4, as "GTAB" is the longest common subsequence.

# Test Case 3
str1 = "ABC"
str2 = "XYZ"
n = len(str1)
m = len(str2)
print(LCS(str1, str2, n, m))  # Output should be 0, as there is no common subsequence.

# Test Case 4
str1 = "ABCD"
str2 = "DCBA"
n = len(str1)
m = len(str2)
print(LCS(str1, str2, n, m))  # Output should be 1, as the only common subsequence is "D".

# Test Case 5
str1 = ""
str2 = "XYZ"
n = len(str1)
m = len(str2)
print(LCS(str1, str2, n, m))  # Output should be 0, as one of the strings is empty.
