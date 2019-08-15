class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s:
            return True
        s = s.lower()
        l = 0
        r = len(s) - 1
        while l < r:
            if s[l].isdigit() or s[l].isalpha():
                if s[r].isdigit() or s[r].isalpha():
                    if s[l] == s[r]:
                        l += 1
                        r -= 1
                    else:
                        return False

                else:
                    r -= 1
            else:
                l += 1
        return True