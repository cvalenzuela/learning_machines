# =========
# Compress - Run Length Encoding.
# Week 1 Learning Machines - Patrick Hebron
# ITP NYU - Fall 2017
#
# Cristobal Valenzuela
# cv965@nyu.edu
# https://en.wikipedia.org/wiki/Run-length_encoding
# =========

def prompt():
  option = input('Do you want to encode or decode? (e/d): ')
  if(option == 'e'):
    user_input = input('String to encode: ')
    encode(user_input)
  elif(option == 'd'):
    user_input = input('String to decode: ')
    decode(user_input)
  else:
    print('Not a valid thing to do!')
    prompt()

def encode(input):
  result = ''
  count = 1
  
  for i, c in enumerate(input):
    if(i != 0):
      if(i < len(input) - 1 and c == input[i+1]):
        count = count + 1
      else:
        result += str(count) + c
        count = 1
    else:
      count += 1
  
  if(len(result) < len(input)):
    print('encode input: ' + result)
  else:
    print('the result ' + result + ' is bigger than the input ' + input)
    print('dont use this to encode')

  prompt()
    
def decode(input):
  result = ''
  multiplier = ''
  
  for i,c in enumerate(input):
    if c.isdigit():
      multiplier += c
    else:
      result += int(multiplier)*c
      multiplier = ''
  print('decode: ' + result)
  prompt()
    
prompt()