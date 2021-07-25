class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        i = 1
        if len(flowerbed) < 2 and flowerbed[0] == 0:
            return True
        count = 0
        if flowerbed[0] == 0 and flowerbed[1] == 0:
            flowerbed[0] = 1
            count += 1
        if flowerbed[-1] == 0 and flowerbed[-2] == 0:
            flowerbed[-1] = 1
            count += 1
        while i < len(flowerbed) - 1 and count != n:
            cur = flowerbed[i]
            prev = flowerbed[i-1]
            nxt = flowerbed[i+1]
            if not (cur or prev or nxt):
                count += 1
                flowerbed[i] = 1
                i += 2
            elif nxt == 1:
                i += 3
            elif cur == 1:
                i += 2
            else:
                i += 1
        return count >= n