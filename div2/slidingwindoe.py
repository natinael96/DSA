# Given an array, find the average of all contiguous subarrays of size ‘K’ in it.

def find_average_of_subarrays(K, arr):
    result = []
    
    i = 0
    j = K
    while j <= (len(arr) - K):
        summ = sum(arr[i:j])
        result.append(summ/K)
        
        i += 1
        j += 1
    return result
        
# Maximum Sum Subarray of Size K (easy)

def max_subarrays_of_size_k(K, arr):
    result = [0]*(len(arr)-K+1)
    
    i = 0
    j = K
    while j <= (len(arr)):
        summ = sum(arr[i:j])
        result[i]=  summ
        
        i += 1
        j += 1
    maxx = max(result)
    return maxx

# Smallest Subarray with a given sum (easy)

def smallest_subarray_with_given_sum(S, arr):
    min_length = float('inf')
    
    for i in range(len(arr)):
        curr_sum = 0
        end = i
        while end < len(arr):
            curr_sum += arr[end]
            end += 1
            
            if curr_sum >= S:
                min_length = min(min_length, end - i) 
            
    if min_length == float('inf'):
        return 0  # If no subarray found
    else:
        return min_length
    
# Longest Substring with K Distinct Characters (medium)

def longest_substring_with_k_distinct(str, K):
    start = 0
    max_length = 0
    char_freq = {}
    
    for end in range(len(str)):
        right = str[end]
        if right not in char_freq:
            char_freq[right] = 0
        char_freq[right] += 1
    
        while len(char_freq) > K:
            left = str[start]
            char_freq[left] -= 1
            if char_freq[left] == 0:
                del char_freq[left]
            start += 1
        max_length = max(max_length, end - start + 1)
    return max_length
            
# Fruits into Baskets (medium)
def fruit_into_baskets(fruits):
    start = 0
    max_length = 0
    freq = {}
    
    for end in range(len(fruits)):
        right = fruits[end]
        if right not in freq:
            freq[right] = 0
        freq[right] += 1
        
        while len(freq) > 2:
            left = fruits[start]
            freq[left] -= 1
            if freq[left] == 0:
                del freq[left]
            start += 1
            
        max_length = max(max_length,end - start + 1)
    
    return max_length
    