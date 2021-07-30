class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        d5, d10 = 0, 0
        for bill in bills:
            # print(bill, d5, d10)
            if bill == 5:
                d5 += 1
            elif bill == 10:
                d10 += 1
                if d5 > 0:
                    d5 -= 1
                else:
                    return False
            else:
                if d10 > 0 and d5 > 0:
                    d10 -= 1
                    d5 -= 1
                elif d5 > 2:
                    d5 -= 3
                else:
                    return False
        return True