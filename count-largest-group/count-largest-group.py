class Solution:
    def countLargestGroup(self, n: int) -> int:
        def sum1(n: int) -> int:
            getsum = 0
            for digit in str(n):
                getsum += int(digit)
            return getsum
        d = {}
        for i in range(1,n+1):
            getsum = sum1(i)
            if getsum in d:
                d[getsum] += 1
            else:
                d[getsum] = 1
        d1 = {}
        print(d)
        max_val = max(d.values())
        # for i in d.values():
        #     if i in d1:
        #         d1[i] += 1
        #     else:
        #         d1[i] = 1
        # return max(d1.values())
        count = 0
        for i in d.values():
            if i == max_val:
                count += 1
        return count