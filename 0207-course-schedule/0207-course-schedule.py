class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        send = [[] for i in range(numCourses)]
        get = [[] for i in range(numCourses)]
        
        for course2, course1 in prerequisites:
            send[course1].append(course2)
            get[course2].append(course1)
            
        queue = []
        done = 0
        
        for index, course in enumerate(get):
            if len(course) == 0:
                queue.append(index)
                get[index].append(-1)
                
        if len(queue) == 0:
            return False
        
        while len(queue) > 0:
            now = queue.pop(0)
            done += 1
            for course in send[now]:
                get[course].remove(now)
                if len(get[course]) == 0:
                    queue.append(course)
                    
        return True if done == numCourses else False
        
        
            
                
        
                    