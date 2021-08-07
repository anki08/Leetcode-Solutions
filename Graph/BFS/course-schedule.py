import collections
class GNode:
    def __init__(self):
        self.inDegrees = 0
        self.outNodes = []
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        graph = collections.defaultdict(GNode)
        for prevCourse, nextCourse in prerequisites:
            graph[prevCourse].outNodes.append(nextCourse)
            graph[nextCourse].inDegrees += 1

        queue = collections.deque()

        for index, node in graph.items():
            if node.inDegrees == 0:
                queue.append(index)

        removed_edges = 0
        while(queue):
            course = queue.popleft()
            for nextCourse in graph[course].outNodes:
                graph[nextCourse].inDegrees -=1
                removed_edges += 1

                if (graph[nextCourse].inDegrees == 0):
                    queue.append(nextCourse)
        if(removed_edges == numCourses):
            return True
        else:
            return False

if __name__ == '__main__':
    sol = Solution()
    print(sol.canFinish(numCourses = 3, prerequisites = [[1,0], [2, 0]]))