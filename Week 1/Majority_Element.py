class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        x=0
        c=1
        for i in range(1,len(nums)):
            if nums[i]==nums[x]:
                c+=1
            else:
                c-=1
            if c==0:
                x=i
                c=1
        return (nums[x])
                
        
