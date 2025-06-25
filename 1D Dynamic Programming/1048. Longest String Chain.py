# ----------------------------- Top-Down Dynamic Programming (Memoization) -----------------------------

class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        word_set = set(words)
        memo = {}

        def dfs(word):
            if word in memo:
                return memo[word]
            max_chain = 1

            for i in range(len(word)):
                pred = word[:i] + word[i + 1:]
                if pred in word_set:
                    current_chain = 1 + dfs(pred)
                    max_chain = max(max_chain, current_chain)
            memo[word] = max_chain
            return max_chain

        result = 0
        for word in words:
            result = max(result, dfs(word))
        return result

# ----------------------------- Bottom-Up Dynamic Programming (Tabulation) -----------------------------

class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=len)
        memo = {}
        max_chain = 1
        for word in words:
            memo[word] = 1
            for i in range(len(word)):
                pred = word[:i] + word[i + 1:]
                if pred in memo:
                    memo[word] = max(memo[word], memo[pred] + 1)

            max_chain = max(max_chain, memo[word])
        return max_chain
