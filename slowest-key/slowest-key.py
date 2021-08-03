class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        releaseTimes = [0] + releaseTimes
        keysPressed = "0" + keysPressed
        out = ""
        dif = 0
        index = 0
        for i in range(1,len(releaseTimes)):
            d = releaseTimes[i] - releaseTimes[i-1]
            if d > dif:
                index = i
                dif = d
            elif d == dif and keysPressed[i] > keysPressed[index]:
                index = i
            else:
                continue
        return keysPressed[index]