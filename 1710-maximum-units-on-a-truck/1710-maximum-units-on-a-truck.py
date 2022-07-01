class Solution(object):
    def maximumUnits(self, boxTypes, truckSize):
        boxTypes = sorted(boxTypes, key = lambda x : x[1], reverse = True)
        now = 0
        answer = 0
        while True:
            if now + boxTypes[0][0] > truckSize:
                answer += boxTypes[0][1] * (truckSize - now)
                break
            else:
                now += boxTypes[0][0]
                answer += boxTypes[0][0] * boxTypes[0][1]
                if len(boxTypes) == 1:
                    break
                else:
                    del boxTypes[0]
        return answer