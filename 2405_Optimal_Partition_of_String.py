'''
Given a string s, partition the string into one or more substrings such that the characters in each substring are unique.
That is, no letter appears in a single substring more than once.

Return the minimum number of substrings in such a partition.

Note that each character should belong to exactly one substring in a partition.
'''

class Solution(object):
    def partitionString(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 1
        seen = set()
        for char in s:
            if char not in seen:
                seen.add(char)
                continue
            seen.clear()
            seen.add(char)
            count +=1
        return count
