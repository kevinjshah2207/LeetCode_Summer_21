class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d = {}
        for i, val in enumerate(nums1):
            d[nums2[i]] = i
        return [d[j] for j in nums1]