from collections import Counter
from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if Counter(s) == Counter(t):
            return True
        return False

# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         if len(s) != len(t):
#             return False

#         seen_s = {}
#         seen_t = {}

#         for char in s:
#             if seen_s.get(char):
#                 seen_s[char] += 1
#             else:
#                 seen_s[char] = 1
        
#         for char in t:
#             if seen_t.get(char):
#                 seen_t[char] += 1
#             else:
#                 seen_t[char] = 1

#         if seen_s == seen_t:
#             return True
        
#         return False



    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        seen_s = defaultdict()
        seen_t = defaultdict()

        for char in s:
            if seen_s.get(char):
                seen_s[char] += 1
            else:
                seen_s[char] = 1

        for char in t:
            if seen_t.get(char):
                seen_t[char] += 1
            else:
                seen_t[char] = 1
        
        if seen_s == seen_t:
            return True
        
        return False