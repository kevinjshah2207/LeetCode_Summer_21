class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        n = len(adjacentPairs) + 1
        ans = []
        for a,b in adjacentPairs:
            adj[a] += [b]
            adj[b] += [a]
        prev = -math.inf
        for k,v in adj.items():
            if len(v) == 1:
                ans += [k]
                break
        while len(ans) < n:
            for next in adj.pop(ans[-1]):
                if next != prev:
                    prev = ans[-1]
                    ans += [next]
                    break
        return ans