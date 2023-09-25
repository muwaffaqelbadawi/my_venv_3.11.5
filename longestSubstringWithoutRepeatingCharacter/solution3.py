# Remeber to communicate with the interviewer while you
# solvoing the problem

"""
    To solve this problem:
    1- generate all the substrings of the given string
    2- Among all substrings having all unique characters
    3- return the maximum length
"""

class Solution:
    def __init__(self, s: str) -> None:
        self.s = s
        self.subArrays = list()
    def subString(self):
        
        for i in range(0, len(self.s)):
            subArray = list()
            for j in range(i, len(self.s)):
                for k in range(i, j+1):
                    subArray.append(self.s[k])
                # subArray.append(self.s[i:j+1])
            self.subArrays.append(subArray)
        return self.subArrays
        
my_solution = Solution("abc")
print(my_solution.subString())

