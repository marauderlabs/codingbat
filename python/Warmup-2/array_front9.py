# https://codingbat.com/prob/p110166

def array_front9(nums):
  l = min(4, len(nums))
  for i in nums[:l]:
    if 9 == i:
      return True
  
  return False

