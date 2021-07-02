class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        l = int(ord(coordinates[0]) - 97)
        n = int(coordinates[1])
        print(l,n)
        if (l+n) % 2 == 0:
            return True
        return False
            