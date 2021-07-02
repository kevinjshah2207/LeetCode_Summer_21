class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        out = []
        intervals = sorted(intervals, key = itemgetter(0), reverse = False)
        l, r = intervals[0][0], intervals[0][1]
        i = 0
        for i in range(len(intervals)):
            if i == 0:
                l = intervals[i][0]
                r = intervals[i][1]
                continue
            if r >= intervals[i][0]:
                r = max(intervals[i][1], r)
            else:
                out.append([l,r])
                l = intervals[i][0]
                r = intervals[i][1]
        if [l,r] not in out:
            out.append([l,r])
        return out