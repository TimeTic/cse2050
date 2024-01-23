def is_anagram(word1, word2):
    """Checking if a word is anagram"""
    return sorted(word1) == sorted(word2)


# print(is_anagram("rat", "thr"))