class Solution:
    def missingNumber(self, arr: List[int]) -> int:
        # d = min(arr[1] - arr[0], arr[2] - arr[1])
        if arr[1] - arr[0] != arr[2] - arr[1]:
            d = arr[-1] - arr[-2]
        else:
            d = arr[1] - arr[0]
        n = arr[0]
        # print(d, n)
        for i in range(1, len(arr)):
            if n+d == arr[i]:
                n += d
            else:
                return n+d
        return arr[0]
            