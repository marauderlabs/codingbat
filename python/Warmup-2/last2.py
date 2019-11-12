# https://codingbat.com/prob/p145834

def last2(str):
  if len(str) < 2:
    return 0

  sub = str[-2:]

  count = 0
  for i in range(len(str)-2):
    if sub == str[i:i+2]:
      count += 1

  return count
