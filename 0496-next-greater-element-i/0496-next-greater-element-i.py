class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        next_greater = {}
        for num in nums2:
            while stack and num > stack[-1]:
                next_greater[stack.pop()] = num
            stack.append(num)
        result = [-1] * len(nums1)
        for i, num in enumerate(nums1):
            if num in next_greater:
                result[i] = next_greater[num]

        return result
