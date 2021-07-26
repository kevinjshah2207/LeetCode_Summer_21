# We keep an index of when a 6 occurs traversing the integer from the back. After traversing
# through the entire number, we get the index of the latest occurrence of 6. Now, we just
# replace this 6 with a 9 by adding 3*(10^index) to the number.

class Solution:
    def maximum69Number (self, num: int) -> int:
        sixidx = -1
        temp = num
        i = 0
        while temp > 0:
            if temp % 10 == 6:
                sixidx = i
            temp //= 10
            i += 1
        return (num + 3*(10**sixidx)) if sixidx != -1 else num
                