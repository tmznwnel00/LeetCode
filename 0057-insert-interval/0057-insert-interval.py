class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        point = 0
        if len(intervals) == 0:
            return [newInterval]
        for i in range(len(intervals)):
            if newInterval[0] >= intervals[i][0]:
                intervals.insert(i + 1, newInterval)
                point = i
                break
            elif newInterval[0] < intervals[i][0]:
                intervals.insert(i, newInterval)
                point = i
                break
        del_list = []
        intervals.sort()
        for i in range(len(intervals) - 1):
            l1 = intervals[i]
            l2 = intervals[i+1]
            if l1[1] >= l2[0]:
                l3 = [min(l1[0], l2[0]), max(l1[1], l2[1])]
                intervals[i] = l3
                intervals[i+1] = l3
                if l1 != l3:
                    del_list.append(l1)
                if l2 != l3:
                    del_list.append(l2)
        intervals = list(map(list,set(list(map(tuple,intervals)))))
        for j in del_list:
            
            while j in intervals:
                intervals.remove(j)
        return sorted(intervals)