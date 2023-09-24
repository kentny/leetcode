from collections import defaultdict

class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        sorted_words = sorted(words, key=len)
        hash_map = defaultdict(int)
        result = 0
        for word in sorted_words:
            max_length = 0
            for i in range(len(word)):
                previous_word = word[:i] + word[i+1:]
                max_length = max(max_length, hash_map[previous_word] + 1)
            hash_map[word] = max_length
            result = max(result, max_length)
        return result

