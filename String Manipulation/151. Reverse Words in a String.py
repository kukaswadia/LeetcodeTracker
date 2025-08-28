class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()

        stack = []
        for word in words:
            stack.append(word)
        
        reversed_words = []
        while stack:
            reversed_words.append(stack.pop())

        return "".join(reversed_words)
    
# ------------------------------------------------------------------------------    

class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()

        reversed_words = words[::-1]

        result = " ".join(reversed_words)
        return result 