class Solution:
    def average(self, salary: List[int]) -> float:
        minSalary=min(salary)
        maxSalary=max(salary)
        if len(salary)<=2:
            return 
        salary.remove(minSalary)
        salary.remove(maxSalary)
        n=len(salary)
        sumOfNum=sum(salary)
        return sumOfNum/n