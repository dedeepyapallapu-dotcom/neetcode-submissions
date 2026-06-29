class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        my={}
        for i in nums:
            if i in my:
                return True
            else:
                my[i]=1
        return False
        