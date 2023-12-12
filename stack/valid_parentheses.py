class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i == "{" or i == "[" or i == "(":
                stack.append(i)
            else:
                if len(stack) == 0:
                    return False

                openingBracket = stack.pop()
                if i == "}" and openingBracket != "{":
                    return False
                elif i == ")" and openingBracket != "(":
                    return False
                elif i == "]" and openingBracket != "[":
                    return False
        
        if len(stack) != 0:
            return False

        return True
