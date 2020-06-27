import re

def is_valid(pattern):
  result = re.search(r'^(\d|[1-9]\d|1\d\d|2([0-4]\d|5[0-5]))\.(\d|[1-9]\d|1\d\d|2([0-4]\d|5[0-5]))\.(\d|[1-9]\d|1\d\d|2([0-4]\d|5[0-5]))\.(\d|[1-9]\d|1\d\d|2([0-4]\d|5[0-5]))$', pattern)
  if result == None:
    return False
  else:
    return True
  
def is_valid_IP(strng):
  lst = strng.split('.')
  print(lst)
  passed = 0
  for sect in lst:
    if sect.isdigit():
      if sect[0] != '0':
        if 0 <= int(sect) <= 255:
          passed += 1
  return passed == 4

result = is_valid_IP('0.0.0.0')
print(result)