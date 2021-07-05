from queue import LifoQueue
class Solution:
    def isValid(self, s: str) -> bool:
        # stack = LifoQueue(maxsize = len(s))
        # for ch in s:
        #     if ch == '(' or ch == '[' or ch == '{':
        #         stack.put(ch)
        #     elif ch == ')' and stack.get() == '(':
        #         stack.get()
        #     elif ch == ']' and stack.get() == '[':
        #         stack.get()
        #     elif ch == '}' and stack.get() == '{':
        #         stack.get()
        #     else:
        #         return False
        # if stack.empty():
        #     return True
        # return False
        if len(s) % 2 != 0:
            return False
        stack = ['N']
        for ch in s:
            if ch == '(' or ch == '[' or ch == '{':
                stack.append(ch)
            elif ch == ')' and stack[-1] == '(':
                stack.pop()
            elif ch == ']' and stack[-1] == '[':
                stack.pop()
            elif ch == '}' and stack[-1] == '{':
                stack.pop()
            else:
                return False
        if len(stack) == 1:
            return True
        return False