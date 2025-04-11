# Problem: Employee Importance - https://leetcode.com/problems/employee-importance/

"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        mapp = {emp.id: emp for emp in employees}
        
        def dfs(emp_id):
            emp = mapp[emp_id]
            impo = emp.importance
            for sub_id in emp.subordinates:
                impo += dfs(sub_id)
            return impo
        
        return dfs(id)