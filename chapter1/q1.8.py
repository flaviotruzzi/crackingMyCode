#!/urs/bin/env python
# -*- coding: utf-8 -*-

# Assume you have a method isSubstring which checks if one word is a substring of
# another. Given two strings, s1 and s2, write code to check if s2 is a rotation
# of s1 using only one call to isSubstring (i.e., “waterbottle” is a rotation of
# “erbottlewat”).

s1 = "cachorro"
s2 = "ocachorr"
s3 = "chorroca"
s4 = "rocachor"
s5 = "cachorra"

def check(s1, s2):
  if s2 in ''.join([s1, s1]):
    return True
  return False

