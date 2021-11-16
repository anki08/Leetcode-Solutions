"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""
from collections import defaultdict

class Solution:
    def getImportance(self, employees, id):
        emp = defaultdict(list)
        emp_val = defaultdict(list)
        for i in range(len(employees)):
            emp[employees[i][0]] = employees[i][2]
            emp_val[employees[i][0]] = employees[i][1]
        print(emp_val)

        def util(empid):

            return emp_val[empid] + sum(util(x) for x in emp[empid])
        return util(id)



if __name__ == '__main__':
    sol = Solution()
    print(sol.getImportance(employees = [[1,5,[2,3]],[2,3,[]],[3,3,[]]], id = 1))