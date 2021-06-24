class Solution:
    def sumZero(self, n: int) -> List[int]:
        ans = []
        l = n//2
        # l *= -1
        for i in range(1,l+1,1):
            ans.append(i)
            ans.append(-i)
        if n % 2 != 0:
            ans.append(0)
        return ans