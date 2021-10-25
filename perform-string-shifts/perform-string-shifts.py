class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        sh = 0
        n = len(s)
        for i, val in enumerate(shift):
            if shift[i][0] == 0:
                sh -= val[1]
            else:
                sh += val[1]
        print(sh)
        sh %= len(s)
        
        ans = ''
        print(sh)
        if sh == 0:
            return s
        elif sh > 0:
            ## Left Shift
            ans += s[n-sh:n]
            ans += s[0:n-sh]
        else:
            ## Right Shift
            ans += s[sh+1:]
            ans += s[0:sh+1]
            
        return ans