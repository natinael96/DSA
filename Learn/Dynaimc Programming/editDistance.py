def editDistance(str1, str2, n, m, insrtCost, deletCost, matchCost, misCost):
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    dp[0][0] = 0

    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0:
                dp[i][j] = j * deletCost  # del cost
            elif j == 0:
                dp[i][j] = i * insrtCost  # ins cost
            else:
                ins = dp[i - 1][j] + insrtCost
                dele = dp[i][j - 1] + deletCost
                sub = dp[i - 1][j - 1] + matchCost if str1[j - 1] == str2[i - 1] else dp[i - 1][j - 1] + misCost
                dp[i][j] = min(ins, dele, sub)

    
    for ch in str1:
        print(f" {ch} ", end="")
    print()
    
    
    align_str1 = ""
    align_str2 = ""
    i, j = m, n  
    while i > 0 or j > 0:
        if i > 0 and j > 0 and str1[j - 1] == str2[i - 1]:
            align_str1 = str1[j - 1] + align_str1
            align_str2 = str2[i - 1] + align_str2
            i -= 1
            j -= 1
        elif i > 0 and dp[i][j] == dp[i - 1][j] + insrtCost:
            align_str1 = "-" + align_str1
            align_str2 = str2[i - 1] + align_str2
            i -= 1
        else:
            align_str1 = str1[j - 1] + align_str1
            align_str2 = "-" + align_str2
            j -= 1

    return align_str1, align_str2, dp[m][n]

str1 = "ATC"
str2 = "TCAG"
n = len(str1)
m = len(str2)
insrtCost, deletCost, matchCost, misCost = 1, 1, 3, 0
aligned_str1, aligned_str2, alignment_score = editDistance(str1, str2, n, m, insrtCost, deletCost, matchCost, misCost)

print("Seq 1:", aligned_str1)
print("Seq 2:", aligned_str2)
print("Score:", alignment_score)
