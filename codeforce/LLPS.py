
## ??????????????????? ###
def is_subsequence(s, sub):
    i, j = 0, 0
    while i < len(s) and j < len(sub):
        if s[i] == sub[j]:
            j += 1
        i += 1
    return j == len(sub)

def find_lexicographically_largest_palindromic_subsequence(s):
    n = len(s)
    left, right = 0, n - 1
    palindrome = ""
    
    # Find characters that appear at least twice
    while left < right:
        if s[left] == s[right]:
            palindrome += s[left]
            left += 1
            right -= 1
        else:
            left += 1

    # If there is no palindrome yet, check if there's a character that appears at least twice
    if not palindrome:
        for i in range(n - 1):
            if s[i] in s[i + 1:]:
                palindrome = s[i]
                break

    # Binary search to find the lexicographically largest subsequence
    low, high = 0, len(palindrome) - 1
    while low <= high:
        mid = (low + high) // 2
        candidate = palindrome[mid:]

        # Check if the candidate subsequence is a valid subsequence in the original string
        if is_subsequence(s, candidate):
            low = mid + 1
        else:
            high = mid - 1

    return palindrome[high+1:]

# Read input
s = input().strip()

# Find and print the lexicographically largest palindromic subsequence
result = find_lexicographically_largest_palindromic_subsequence(s)
print(result)
