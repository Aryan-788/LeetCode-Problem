''' We can scramble a string s to get a string t using the following algorithm:

If the length of the string is 1, stop.
If the length of the string is > 1, do the following:
Split the string into two non-empty substrings at a random index, i.e., if the string is s, divide it to x and y where s = x + y.
Randomly decide to swap the two substrings or to keep them in the same order. i.e., after this step, s may become s = x + y or s = y + x.
Apply step 1 recursively on each of the two substrings x and y.
Given two strings s1 and s2 of the same length, return true if s2 is a scrambled string of s1, otherwise, return false.
'''
 
  class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        if len(s1)!=len(s2):
            return False
        m=dict()
        def f(a,b):
            if (a,b) in m:
                return m[(a,b)]
            if a==b:
                m[a,b]=True
                return True
            if len(a)!=len(b):
                m[(a,b)]=False
                return False
            
            for i in range(1,len(a)):
                if f(a[:i],b[:i]) and f(a[i:],b[i:]):
                    m[(a,b)]=True
                    return True
                if f(a[:i],b[-i:]) and f(a[i:],b[:len(a)-i]):
                    m[(a,b)]=True
                    return True
                
            m[(a,b)]=False
            return False
        return f(s1,s2)
