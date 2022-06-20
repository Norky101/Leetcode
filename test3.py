def targetsum(target, nums):
    for i in range(len(nums)):
     for j in range(len(nums)):
        if nums[i] + nums[j] == target and i != j:
          return i, j

            #print( "vals", nums[i], nums[j])


#nums1 = [2,7,11,15]
#target1 = 9
# Output 0,1
#print ("result3",targetsum(target1, nums1), "correct")

#nums2 = [3,3]
#target2 = 6
# output 0,1   # should be corect
#print ("result2",targetsum(target2, nums2))

nums3 = [3,2,4]
target3 = 6
# Output 1,2
print ("result1", targetsum(target3, nums3))