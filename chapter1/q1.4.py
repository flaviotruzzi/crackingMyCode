#!/usr/bin/env python

# Write a method to decide if two strings are anagrams or not.

#check if two strings are anagrams
# aba -> aab

from collections import Counter

s1 = 'babaca'
s2 = 'cabaca'
s3 = 'bacaba'

# using counter
def checkAnagram(s1, s2):
  s1 = Counter(s1)
  s2 = Counter(s2)
  for key in s1:
    if key not in s2:
      return False
    if s1[key] != s2[key]:
      return False
  return True

# sorting
def checkAnagram2(s1, s2):
  return sorted(s1) == sorted(s2)

