# https://codingbat.com/prob/p182414

def string_match(a, b):
  shorter = min(len(a), len(b))
  count = 0
  
  for i in range(shorter-1):
    count += int(a[i:i+2] == b[i:i+2])
      
  return count

