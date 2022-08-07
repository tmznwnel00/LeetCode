class Solution(object):
    def taskSchedulerII(self, tasks, space):
        """
        :type tasks: List[int]
        :type space: int
        :rtype: int
        """
        now = 1
        d = {}
        d[tasks[0]] = now
        for i in range(1, len(tasks)):
            now += 1
            if tasks[i] not in d:
                d[tasks[i]] = now
            else:
                if now > d[tasks[i]] + space:
                    d[tasks[i]] = now
                else:
                    now = d[tasks[i]] + space + 1
                    d[tasks[i]] = now
        return now