class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        pre_of = {}
        pre = {}
        available = list(range(numCourses))
        for prerequisite in prerequisites:
            if prerequisite[1] in pre_of:
                pre_of[prerequisite[1]].append(prerequisite[0])
            else:
                pre_of[prerequisite[1]] = [prerequisite[0]]
            if prerequisite[0] in pre:
                pre[prerequisite[0]].append(prerequisite[1])
            else:
                pre[prerequisite[0]] = [prerequisite[1]]
            if prerequisite[0] in available:
                available.remove(prerequisite[0])
        solution = []
        while len(available) > 0:
            take = available[0]
            solution.append(take)
            available.pop(0)
            if take in pre_of:
                for course in pre_of[take]:
                    if len(pre[course]) == 1:
                        available.append(course)
                    else:
                        pre[course].remove(take)
        if len(solution) == numCourses:
            return solution
        return []