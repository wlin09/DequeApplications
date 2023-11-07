import sys
from Stack import Stack

def delimiter_check(filename):
  stack = Stack()
  with open(filename, 'r') as file:
    text = file.read()
  for char in text:
    if char in '([{':
      stack.push(char)
    elif char in ')]}':
      char_2 = stack.pop()
      if not (char_2 + char in '()' or char_2 + char in '[]' or char_2 + char in '{}'): # reduce if statements
        return False
  return True

if __name__ == '__main__':
  if len(sys.argv) < 2:
    print('Usage: python Delimiter_Check.py file_to_check.py')
  else:
    if delimiter_check(sys.argv[1]):
      print('The file contains balanced delimiters.')
    else:
      print('The file contains IMBALANCED DELIMITERS.')