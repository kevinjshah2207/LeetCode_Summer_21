class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        items.sort(key=lambda x:(x[0], -x[1]))
        # print(items)
        sid = items[0][0]
        marks = 0
        count = 0
        ans = []
        for i, val in enumerate(items):
            if count == 5 and sid == val[0]:
                continue
            elif count == 5 and sid != val[0]:
                count = 0
                marks = 0
                sid = val[0]
            if sid == val[0]:
                marks += val[1]
                count += 1
                if count == 5:
                    ans.append([sid, marks//5])
                    continue
        return ans