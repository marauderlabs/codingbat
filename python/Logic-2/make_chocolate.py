# https://codingbat.com/prob/p190859

def make_chocolate(small, big, goal):
  if goal < big*5:
    big = goal//5
  
  goal -= big*5
  
  return goal if goal <= small else -1
