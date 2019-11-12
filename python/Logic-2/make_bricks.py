# https://codingbat.com/prob/p118406

def make_bricks(small, big, goal):
  
  # if we have too many big bricks then use only as much as we need.
  if big*5 > goal:
    big = goal//5
  
  # remaining?
  goal -= big*5
  
  # enough smalls left?
  return small >= goal
  

