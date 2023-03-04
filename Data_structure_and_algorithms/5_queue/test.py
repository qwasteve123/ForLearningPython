def removeDuplicates(nums):
    pointer = 0
    if not nums:
        return []
    if len(nums) == 1:
        return nums
    for i in range(len(nums)-1):
        if  nums[i+1] != nums[i]:
            nums[pointer+1] = nums[i+1]
            pointer = 1
    return pointer
    # if pointer != len(nums):
    #     for i in range(pointer,len(nums)):
    #         nums[i] = '_'
    # return nums

x = removeDuplicates([0,0,1,1,1,2,2,3,3,4])
pass