class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
    


        prereq = [set() for _ in range(numCourses)]
        next_courses = [[] for _ in range(numCourses)]

        for i in range(len(prerequisites)):
            course = prerequisites[i]
            prereq[course[0]].add(course[1])
            next_courses[course[1]].append(course[0])

        q = deque()
        vis = [0]*numCourses
        for i in range(numCourses):
            if not prereq[i]:
                q.append(i)

        if not q:
            return False

        while q:
            course = q.popleft()
            vis[course] = 1
            for next_course in next_courses[course]:
                prereq[next_course].remove(course)
                if not prereq[next_course]:
                    q.append(next_course)
        
        
        for v in vis:
            if v == 0:
                return False

        return True

# prereqs
# next_courses - 

# find all courses which do not have prereqs (no keys) -- start of bfs . put in queue


# for each course:
#     once it is done, iterate next courses, and remove this from prereq. 
#     if prereq becomes empty, add to queue

