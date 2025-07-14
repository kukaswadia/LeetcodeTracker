class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        lst = path.split("/")
        for d in lst:
            if d == "..":
                if stack:
                    stack.pop()
            elif d != "" and d != ".":
                stack.append(d)

        return "/" + "/".join(stack)
