from typing import List

def removeDuplicates(nums: List[int]) -> int:
    
    newnums = []
    for i in range(1,len(nums)):
        if nums[i] not in newnums:
            newnums.append(nums[i])
    return newnums

print(removeDuplicates([0,0,1,1,1,2,2,3,3,4]))