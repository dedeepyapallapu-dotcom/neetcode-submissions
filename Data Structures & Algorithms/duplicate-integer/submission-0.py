class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        my_d={}
        for i in nums:
            if i in my_d:
                return True
            else:
                my_d[i]=1
        return False