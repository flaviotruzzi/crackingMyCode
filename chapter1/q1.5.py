#!/usr/bin/env python

# Write a mathod to replace all spaces in a string with '%20'.

def replaceSpaces(s):
  return s.replace(' ','%20')

# I think it needs to use char arrays to be more difficult
from array import *
def replaceSpaces2(s): #
  s = array('c', list(s))
  spaces = s.count(' ')

  newString = array('c', [])
  for i in s:
    if i is not ' ':
      newString.append(i)
    else:
      newString.append('%')
      newString.append('2')
      newString.append('0')
  return ''.join(newString)

def replaceSpaces3(s):
  k = []
  for i in s:
    if i is not ' ':
      k.append(i)
    else:
      k.append('%20')
  return ''.join(k)

