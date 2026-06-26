class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d={}
        for i, n in enumerate(nums):
            diff = target-n
            if diff in d:
                return [d[diff], i]
            d[n]=i

          

        
#NOTES
#create an empty dictionary, store each number we already saw and its index
#loops through list, i is the index and n is the number at that index
#finds the number we need to pair with the current number to reach the target
#checks if that needed number was already seen earlier. 
#If it was, return [prevMap[diff], i] returns the index of the earlier number and the current index. 
#If not, prevMap[n] = i saves the current number and its index so it can be used later.