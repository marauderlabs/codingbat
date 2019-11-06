# https://codingbat.com/prob/p166884

def parrot_trouble(talking, hour):
    if talking and (hour < 7 or hour > 20):
        return True
    else: 
        return False

def parrot_trouble_ternary(talking, hour):
  return True if talking and (hour < 7 or hour > 20) else False

