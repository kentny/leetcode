import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        converted_str = re.sub(r'[^a-zA-Z0-9]', '', s.lower())

        for i in range(int(len(converted_str) / 2)):
            if converted_str[i] is not converted_str[-i-1]:
                return False
        return True
