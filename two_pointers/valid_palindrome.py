class Solution:
    def isPalindrome(self, s: str) -> bool:

        s = s.replace(" ", "")
        s = s.lower()
        if len(s) == 0:
            return True
        print(s)
        i = 0
        j = len(s) - 1
        while i != j and i < len(s) and j >= 0:
            print(i, j)
            if s[j].isalnum() is False:
                j -= 1
                continue
            elif s[i].isalnum() is False:
                i += 1
                continue

            if s[i] != s[j]:
                return False
            i += 1
            j -= 1

        return True
