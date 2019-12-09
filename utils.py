import math

def splitby2(x):
  '''
  split x to a power polynomial of 2
  return:
    list
  '''
  if x == 1:
    return [0]
  elif x == 0:
    return []
  else:
    bit = int(math.log2(x))
    release = x - 2**bit
    result = [bit]
    result.extend(splitby2(release))
    return result

def sumby2(x):
  result = 0
  for v in x:
    result += 2**v
  return result

# x = sumby2(splitby2(x))
# splitby(396000) = [18, 17, 11, 9, 7, 6, 5] = 2**18 + 2**17 + 2**11 + 2**9 + 2**7 + 2**6 + 2**5
