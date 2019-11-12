# https://codingbat.com/prob/p107863

def lucky_sum(a, b, c):
  l = [a, b, c]
  s = 0
  for i in l:
    if i == 13: break
    s += i
  return s

