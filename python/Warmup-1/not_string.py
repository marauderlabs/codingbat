# https://codingbat.com/prob/p189441

def not_string(str):
  if len(str) < 3 or str[:3] != 'not':
    return 'not ' + str
  
  else:
    return str

