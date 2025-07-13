class Solution:
    def isValid(self, s: str) -> bool:
        d = {"(": ")", "{": "}", "[": "]"}
        stack = []
        for char in s:
            if char in d:  # every single open parentheses is a key in the dictionary
                stack.append(char)
            else:
                if stack == [] or d[stack.pop()] != char: # check the value of that key in the dictionary
                    return False
        return True if stack == [] else False