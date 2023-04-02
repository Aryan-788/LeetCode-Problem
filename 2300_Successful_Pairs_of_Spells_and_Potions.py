'''
You are given two positive integer arrays spells and potions, of length n and m respectively, where spells[i] represents the strength of the ith spell and 
potions[j] represents the strength of the jth potion.

You are also given an integer success. A spell and potion pair is considered successful if the product of their strengths is at least success.

Return an integer array pairs of length n where pairs[i] is the number of potions that will form a successful pair with the ith spell.
'''

class Solution:
    def successfulPairs(self, spells, potions, success):
        sorted_potions = sorted(potions)
        result = []
        for a in spells:
            count = len(sorted_potions) - bisect_left(sorted_potions, (success + a - 1) // a)
            result.append(count)
        return result
