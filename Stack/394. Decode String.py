class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for char in s:
            if char != "]":
                stack.append(char)
            else:
                cur = ""
                while stack and stack[-1] != "[":
                    cur = stack.pop() + cur
                stack.pop()
                num = ""
                while stack and stack[-1].isdigit():
                    num = stack.pop() + num
                stack.append(cur * int(num))
        return "".join(stack)