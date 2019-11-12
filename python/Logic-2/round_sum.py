# https://codingbat.com/prob/p179960

def round_sum(a, b, c):
  l = [a, b, c]
  s = 0
  for i in l:
    s += round10(i)
  return s
  
def round10(n):
  if n%10 < 5:
    return n - n%10
  else:
    return n + (10 - n%10)

