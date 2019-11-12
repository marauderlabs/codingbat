# https://codingbat.com/prob/p193604

def array123(nums):
  if len(nums) < 3:
    return False
  
  for i in range(len(nums)-2):
    if [1,2,3] == nums[i:i+3]:
      return True
  
  return False

