def is_anagram(word1, word2):
    """Checks if a word is anagram"""
    return sorted(word1) == sorted(word2)