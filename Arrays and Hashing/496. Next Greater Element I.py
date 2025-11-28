class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        next_greater = {}
        stack = []

        for num in nums2:
            # While stack is not empty and current num is greater than stack top
            # Found the next greater element for stack top
            while stack and num > stack[-1]:
                smaller = stack.pop()
                next_greater[smaller] = num

            # Push the current number to stack 
            stack.append(num)

        # Elements still in stack have no next greater element 
        while stack:
            next_greater[stack.pop()] = -1

        # Build result array by looking up each element from nums2
        return [next_greater[num] for num in nums1]