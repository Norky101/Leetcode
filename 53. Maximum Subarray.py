def maxsubarray(nums):

    maxSub = nums[0]
    curSum = 0

    for n in nums:
        if curSum  < 0:
            curSum  = 0
        curSum += n
        maxSub = max(maxSub, curSum )

    return maxSub


nums = [2,3,-3,-5, 3,2,1,-2]
aa = maxsubarray(nums)
print (aa)