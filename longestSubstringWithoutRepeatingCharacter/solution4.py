class solution:
    def __init__(self) -> None:
        self.left = 0
        self.right = 0
        self.longest_substring = 0
        self.uniqueCharacter = list()
    
    def longest_substring_without_repeating_char(self, s: str):
        while(self.right < len(s)):
            if s[self.right] not in self.uniqueCharacter:
                self.uniqueCharacter.append(s[self.right])
                self.right+=1
                self.longest_substring = max(self.longest_substring, len(self.uniqueCharacter))
            else:
                self.uniqueCharacter[self.left]
                self.left+=1
        return self.longest_substring
    
my_solution = solution()
my_solution.longest_substring_without_repeating_char("abcabcbb")