# https://codingbat.com/prob/p143951

def lone_sum(a, b, c):
  if a == b and a == c:
    return 0
  if a == b:
    return c
  if b == c:
    return a
  if a == c:
    return b
  return a + b + c

