class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        # return (set([path[1] for path in paths]) - set([path[0] for path in paths])).pop()
        if len(paths) == 1:
            return paths[0][1]
        d = {}
        for i in range(len(paths)):
            if paths[i][1] in d:
                d[paths[i][1]] -= 1
            else:
                d[paths[i][1]] = 1
        
            if paths[i][0] in d:
                d[paths[i][0]] -= 1
            else:
                d[paths[i][0]] = 0
        for key, value in d.items():
            if value == 1:
                return key
            