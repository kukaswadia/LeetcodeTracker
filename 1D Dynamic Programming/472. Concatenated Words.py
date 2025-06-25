# ----------------------------- Brute Force (Recursive Backtracking) -----------------------------

class Solution:
    def isConcatenatedWord(self, word, word_set):
        def canForm(word):
            if not word:
                return True

            for i in range(1, len(word) + 1):
                prefix = word[:i]
                if prefix in word_set and canForm(word[i:]):
                    return True
            return False
        return canForm(word)

    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        concatenated_words = []
        word_set = set(words)
        for word in words:
            if not word:
                continue
            word_set.remove(word)
            if self.isConcatenatedWord(word, word_set):
                concatenated_words.append(word)
            word_set.add(word)
        return concatenated_words

# ----------------------------- Top-Down Dynamic Programming (Memoization) -----------------------------

class Solution:
    def isConcatenatedWord(self, word, word_set):
        memo = {}
        def canForm(word):
            if word in memo:
                return memo[word]

            if not word:
                return True

            for i in range(1, len(word) + 1):
                prefix = word[:i]
                if prefix in word_set and canForm(word[i:]):
                    memo[word] = True
                    return True

            memo[word] = False
            return False
        return canForm(word)

    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        concatenated_words = []
        word_set = set(words)
        for word in words:
            if not word:
                continue
            word_set.remove(word)
            if self.isConcatenatedWord(word, word_set):
                concatenated_words.append(word)
            word_set.add(word)
        return concatenated_words

# ----------------------------- Bottom-Up Dynamic Programming (Tabulation) -----------------------------

class Solution:
    def canForm(self, word, word_set):
        n = len(word)
        dp = [False] * (n + 1)
        dp[0] = True

        for i in range(1, n + 1):
            for j in range(0, i):
                if dp[j] and word[j:i] in word_set:
                    dp[i] = True
                    break
        return dp[n]

    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        concatenated_words = []
        word_set = set(words)

        for word in words:
            if not word:
                continue
            word_set.remove(word)
            if self.canForm(word, word_set):
                concatenated_words.append(word)
            word_set.add(word)
        return concatenated_words