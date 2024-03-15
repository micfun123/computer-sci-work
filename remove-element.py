def removeElement(self, nums: List[int], val: int) -> int:
    for i in range(nums.count(val)):
        nums.remove(val)