class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        n=len(s)
        if n==0:
            return True
        if n==1:
            return False
        if s[0] in [')',']','}']:
            return False
        for i in range(n):
            if s[i]=='(' or s[i]=='[' or s[i]=='{':
                stack.append(s[i])
            elif s[i]==')' and stack and stack[-1]=='(':
                stack.pop()
            elif s[i]==']' and stack and stack[-1]=='[':
                stack.pop()
            elif s[i]=='}' and stack and stack[-1]=='{':
                stack.pop()
            else:
                return False
        return stack == []
            