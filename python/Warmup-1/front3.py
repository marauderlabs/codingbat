# https://codingbat.com/prob/p147920

def front3(str):
  front = ""
  if len(str) <= 3:
    front = str
  else:
    front = str[:3]
  
  return front*3

