#!/usr/bin/env python

# with buffer and unordered
s = 'aabbccd'
s = "".join(set(s))

# with buffer and ordered and O(n)
s = 'aabbccd'
result = []
for i in s:
  if i not in result:
    result.append(i)

# without buffer but O(n^2)
s = 'aabbccd'
#using chararray, since python string is immutable
def removeDuplicates(sa):
  tail = 1
  l = len(sa)
  for i in xrange(tail, l):
    for j in xrange(tail):
      if j < i and sa[i] == sa[j]:
        sa[i] = ''
    tail += 1
  #answer is in sa, just returning s string for idk
  return ''.join(sa)
