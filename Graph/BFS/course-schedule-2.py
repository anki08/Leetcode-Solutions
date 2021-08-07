from collections import deque, defaultdict
class GNode:
    def __init__(self):
        self.inDegrees = 0
        self.outNodes = []

class Solution:
    def findOrder(self, numCourses, prerequisites):
        if (len(prerequisites) == 0 and numCourses > 0):
            return [i for i in range(numCourses)]
        graph = defaultdict(GNode)
        val = 0
        for nextCourses, prevCourses in prerequisites:
            graph[prevCourses].outNodes.append(nextCourses)
            graph[nextCourses].inDegrees += 1
            val += 1

        res = []
        queue  = deque()
        for index, node in graph.items():
            if node.inDegrees == 0:
                queue.append(index)
                res.append(index)
        removed_edges = 0
        while queue:
            curr = queue.popleft()
            for nextCourse in graph[curr].outNodes:
                graph[nextCourse].inDegrees -= 1
                removed_edges += 1

                if(graph[nextCourse].inDegrees == 0):
                    queue.append(nextCourse)
                    res.append(nextCourse)

        # if (len(prerequisites) == 0 and numCourses > 0):
        #     res = [i for i in range(numCourses)]
        if(len(res) < numCourses and val == removed_edges):
            # print(res)
            res = res[::-1]
            lis = []
            for i in  range(numCourses):
                if i not in res:
                    lis.append(i)

            res.extend(lis)
            res = res[::-1]
        return res if len(res) == numCourses  else []



if __name__ == '__main__':
    sol = Solution()
    print(sol.findOrder(numCourses = 2, prerequisites = [[1,0]]))
    print(sol.findOrder(numCourses = 3, prerequisites = [[1,0]]))
    print(sol.findOrder(numCourses = 2, prerequisites = []))
    print(sol.findOrder(numCourses = 2, prerequisites = [[0,1],[1,0]]))
    print(sol.findOrder(numCourses = 4, prerequisites = [[3,0],[0,1]]))