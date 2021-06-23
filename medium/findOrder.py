from collections import defaultdict
WHITE = 1
GRAY = 2
BLACK = 3

def findOrder(numCourses, prerequisites):

    result = []
    adj_list = defaultdict(list)
    color = {k: WHITE for k in range(numCourses)}
    print(color)
    for course, prereq in prerequisites:
        adj_list[prereq].append(course)
    print(adj_list)
    is_possible = True

    def dfs(node):
        nonlocal is_possible

        if is_possible == False:
            return

        color[node] = GRAY
        if node in adj_list:
         for vertex in adj_list[node]:
            if color[node] == WHITE:
                dfs(vertex)
            if color[node] == GRAY:
                is_possible = False

        color[node] = BLACK
        result.append(node)



    for i in range(numCourses):
        if(color[i] == WHITE):
            dfs(i)

    return result[::-1] if is_possible else []





if __name__ == '__main__':
    findOrder(4, [[1,0],[2,0],[3,1],[3,2]])