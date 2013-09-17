#!/usr/bin/env python

# Implement and algorithm to determine if a string has all unique character.
# What if you can not use additional data structures?

import sys
from collections import Counter

def checkString(str):
  """Print the character"""
  str.upper()
  d = dict()
  for c in str:
    if c not in d:
      d[c] = ''
    else:
      print "Character repeated:", c

def checkString2(str):
  """Count the repeated"""
  g = Counter(str)

def checkString3(str):
  """Smart one"""
  checker = 0
  for c in str:
    if (checker & (1 << ord(c))):
      return False
    checker |= (1 << ord(c))
  return True

if __name__ == "__main__":
  checkString(sys.argv[1])              
     
