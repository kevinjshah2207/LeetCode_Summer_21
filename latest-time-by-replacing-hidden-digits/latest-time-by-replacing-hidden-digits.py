class Solution:
    def maximumTime(self, time: str) -> str:
        l = list(time)
        if l[4] == "?":
            l[4] = "9"
        if l[3] == "?":
            l[3] = "5"
        if l[1] == "?" and l[0] == "?":
            l[0] = "2"
            l[1] = "3"
        if l[0] == "?": 
            if l[1] <= "3":
                l[0] = "2"
            else:
                l[0] = "1"
        if l[1] == "?":
            if l[0] == "2":
                l[1] = "3"
            else:
                l[1] = "9"
        return "".join(l)