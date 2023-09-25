# sample_input = [-1,2,3,1,-3,2]    size=2

def hashFunction(string_key: str, bucket_num):
    hash_var = 0
    hash_var += ord(string_key)
    index = hash_var % bucket_num
    return index

class Solution:
    def __init__(self) -> None:
        self.subArrays = list()
        self.bucket_num = 4
    
    def findSubArrays(self, s: str):
        n = len(s)
        for i in range(0, len(str)):
            for j in range(0, n - i):
                for k in range(i, i + j):
                    pass
        