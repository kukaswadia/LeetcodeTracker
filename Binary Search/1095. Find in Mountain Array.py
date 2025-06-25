class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        length = mountainArr.length()

        left, right = 1, length - 2
        while left <= right:
            mid = (left + right) // 2
            leftVal, midVal, rightVal = mountainArr.get(mid - 1), mountainArr.get(mid), mountainArr.get(mid + 1)
            if leftVal < midVal < rightVal:
                left = mid + 1

            elif leftVal > midVal > rightVal:
                right = mid - 1

            else:
                break

        peak = mid

        left, right = 0, peak
        while left <= right:
            mid = (left + right) // 2
            midVal = mountainArr.get(mid)
            if midVal < target:
                left = mid + 1

            elif midVal > target:
                right = mid - 1

            else:
                return mid

        left, right = peak, length - 1
        while left <= right:
            mid = (left + right) // 2
            midVal = mountainArr.get(mid)
            if midVal > target:
                left = mid + 1

            elif midVal < target:
                right = mid - 1

            else:
                return mid

        return -1