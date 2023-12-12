from collections import defaultdict


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict_of_s_letters = defaultdict(int)
        dict_of_t_letters = defaultdict(int)

        for i in s:
            if i in dict_of_s_letters:
                dict_of_s_letters[i] += 1
            else:
                dict_of_s_letters[i] = 1

        for i in t:
            if i in dict_of_t_letters:
                dict_of_t_letters[i] += 1
            else:
                dict_of_t_letters[i] = 1

        for i in s:
            if dict_of_s_letters[i] != dict_of_t_letters[i]:
                return False

        for i in t:
            if dict_of_s_letters[i] != dict_of_t_letters[i]:
                return False

        return True
