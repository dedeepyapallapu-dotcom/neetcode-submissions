class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        d={}
        for num in nums:
            if num in d:
                return True
            d[num]=1
        return False
        
#NOTES
#creating dictionary for each number and its counts 
#going through input and adding numbers each time they appear
#if already in dictionary, then returns False
#else, goes through all numbers with no duplicate --> returns False