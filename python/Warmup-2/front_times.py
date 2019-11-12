# https://codingbat.com/prob/p165097

def front_times(str, n):
  front_len = 3
  front = ""
  
  if len(str) <= front_len:
    front = str
  else:
    front = str[:3]
  
  return front*n

