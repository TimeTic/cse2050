
def contains_permutation(input_string, pattern):
    """The function checks wheter the input_string contains permutations and if does it returns the results"""
    pattern_length = len(pattern)
    pattern_freq = {}
    for char in pattern:
        pattern_freq[char] = pattern_freq.get(char, 0) + 1
    
    window_freq = {}
    start = 0
    end = 0
    
    while end < len(input_string):
        end_char = input_string[end]
        window_freq[end_char] = window_freq.get(end_char, 0) + 1
        
        if end - start + 1 == pattern_length:
            if window_freq == pattern_freq:
                return True
            
            start_char = input_string[start]
            window_freq[start_char] -= 1
            if window_freq[start_char] == 0:
                del window_freq[start_char]
            start += 1
            
        end += 1
    
    return False

result1 = contains_permutation('abcdef', 'cab')
print(result1)  

result2 = contains_permutation('keyboard', 'boy')
print(result2)  

result3 = contains_permutation('patriots', 'sit')
print(result3)  


# word_list=['abcdef', 'cab','keyboard', 'boy','patriots', 'sit']
# for word in word_list:
#     if word in word:
#         print(word)
