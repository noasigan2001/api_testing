from collections import deque

def is_valid_step(word1, word2):
    if len(word1) != len(word2):
        return False
    return sum(1 for c1, c2 in zip(word1, word2) if c1 != c2) == 1

def word_ladder_length(start, end, word_list):
    word_set = set(word_list)
    if end not in word_set:
        return -1