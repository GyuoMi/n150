class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1 
        while l < r:
            # same condition, just to ensure l and r ptr do not cross
            while l < r and not self.alphaNum(s[l]):
                l += 1
            while r > l and not self.alphaNum(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l, r = l + 1, r - 1
        return True

    def alphaNum(self, c):
        # ascii 65-90 for A-Z, 
        # regardless get ascii using ord
        return (ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9')) 
        
