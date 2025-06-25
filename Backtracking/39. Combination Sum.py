class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []

        def comb(curr, start, target):
            if target == 0:
                result.append(curr)
                return

            for i in range(start, len(candidates)):
                if candidates[i] > target:
                    break

                comb(curr + [candidates[i]], i, target - candidates[i])
            return

        comb([], 0, target)
        return result