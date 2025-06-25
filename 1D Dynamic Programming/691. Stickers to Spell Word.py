# DFS with Memoization (Optimized Recursion)

class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        sticker_counts = [Counter(sticker) for sticker in stickers]
        memo = {}
        memo[""] = 0

        def dfs(remaining_target):
            remaining_target = ''.join(sorted(remaining_target))
            if remaining_target in memo:
                return memo[remaining_target]

            target_count = Counter(remaining_target)
            min_needed = float('inf')

            for sc in sticker_counts:
                if remaining_target[0] not in sc:
                    continue
                new_target = []
                for char in target_count:
                    remain = target_count[char] - sc.get(char, 0)
                    new_target.extend([char] * max(remain, 0))
                new_target = ''.join(new_target)
                sub_problem = dfs(new_target)
                if sub_problem != -1:
                    min_needed = min(min_needed, 1 + sub_problem)
            memo[remaining_target] = -1 if min_needed == float('inf') else min_needed
            return memo[remaining_target]

        return dfs(target)
