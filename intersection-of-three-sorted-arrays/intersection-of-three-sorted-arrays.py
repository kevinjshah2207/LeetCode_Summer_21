class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        d1 = {}
        for i, val in enumerate(arr1):
            if arr1[i] not in d1:
                d1[val] = 1
        
        for i, val in enumerate(arr2):
            if arr2[i] in d1:
                d1[val] += 1
        
        for i, val in enumerate(arr3):
            if arr3[i] in d1:
                d1[val] += 1
        
        ans = []
        for i in d1:
            if d1[i] == 3:
                ans.append(i)
        ans.sort()
        return ans