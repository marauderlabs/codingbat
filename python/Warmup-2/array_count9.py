# https://codingbat.com/prob/p166170

def array_count9(nums):
  count = 0
  for i in nums:
    count += int(i==9)
  return count

#from collections import Counter
#
#def array_count9(nums):
#  c = Counter(nums)
#  return c.get(9, 0)
