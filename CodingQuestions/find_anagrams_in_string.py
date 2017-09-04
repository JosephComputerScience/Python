"""
Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.

The order of output does not matter.
"""
from collections import Counter
class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        p_counter = Counter(p)
        s_counter = Counter(s[:len(p) -1 ])
        result = []
        for i in range(len(p) - 1, len(s)):
            s_counter[s[i]] += 1
            if s_counter == p_counter:
                result.append(i-(len(p) -1))
            s_counter[s[i - len(p) + 1]] -= 1
            if s_counter[s[i-len(p) + 1]] == 0:
                del s_counter[s[i - len(p) + 1]]
        
        return result
