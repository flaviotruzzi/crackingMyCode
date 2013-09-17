#!/usr/bin/env python

# Write code to reverse a C-Style String

string = "abcdef\0"

result = string[:-1][::-1] + '\0'

# using arrays...
s = list(string)
for i in xrange((len(s) - 1)/2):
  s[i], s[len(s)-2-i] = s[len(s)-2-i], s[i]


