# https://codingbat.com/prob/p118366

def string_splosion(str):
  out = ""
  for i in range(1, len(str)+1):
    out += str[:i]
  return out

