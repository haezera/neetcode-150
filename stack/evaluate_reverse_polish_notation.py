class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        curr = 0
        total = 0
        for i in tokens:
            if i == "+":
                one = stack.pop()
                two = stack.pop()
                curr = one + two
                stack.append(curr)
            elif i == "*":
                one = stack.pop()
                two = stack.pop()
                curr = int(one) * int(two)
                stack.append(curr)
            elif i == "/":
                one = stack.pop()
                two = stack.pop()
                curr = int(int(two) / int(one))
                stack.append(curr)
            elif i == "-":
                one = stack.pop()
                two = stack.pop()
                curr = int(two) - int(one)
                stack.append(curr)
            else:
                stack.append(int(i))
        
        return stack[0]
