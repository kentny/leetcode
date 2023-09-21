from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len1 = len(s1)
        len2 = len(s2)
        if len1 > len2:
            return False

        counter1 = Counter(s1)
        counter2 = Counter(s2[:len1])

        for i in range(0, len2 - len1 + 1):
            if counter1 == counter2:
                return True

            if counter2[s2[i]] == 1:
                del counter2[s2[i]]
            else:
                counter2[s2[i]] -= 1

            if i + len1 < len2:
                counter2[s2[i + len1]] += 1

        return False
