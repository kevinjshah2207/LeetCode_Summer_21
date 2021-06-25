class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes = sorted(boxTypes, key = itemgetter(1), reverse = True)
        total = 0
        i = 0
        while truckSize > 0 and i < len(boxTypes):
            if boxTypes[i][0] <= truckSize:
                total += (boxTypes[i][0] * boxTypes[i][1])
                truckSize -= boxTypes[i][0]
                i += 1
            else:
                total += (truckSize * boxTypes[i][1])
                i += 1
                break
        return total