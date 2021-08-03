class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        count = collections.defaultdict(list)
        for i, size in enumerate(groupSizes):
            count[size].append(i)
        res = []
        for s,l in count.items():
            for i in range(0,len(l),s):
                res.append(l[i:i+s])
        return res