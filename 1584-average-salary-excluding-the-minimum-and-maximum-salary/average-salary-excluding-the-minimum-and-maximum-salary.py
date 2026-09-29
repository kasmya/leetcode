class Solution:
    def average(self, salary: list[int]) -> float:
        max = salary[0]
        min = salary[0]
        for i in salary:
            if i>max:
                max = i
            if i<min:
                min = i
        total = 0
        for i in salary:
            total += i
        total = total - max - min
        average = total/(len(salary)-2)
        return average
