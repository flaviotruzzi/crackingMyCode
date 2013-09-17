#!/urs/bin/env python

# Write an algorithm such that if an element in an MxN matrix is 0, its entire
# row column is set to 0

from numpy import *

N = 10
M = 5
img = random.randint(10, size=(N,M)).tolist()

def checkAndSet(img, N, M):
  zeros = []
  for i in xrange(N):
    for j in xrange(M):
      if img[i][j] == 0:
        zeros.append((i,j))
  for zero in zeros:
    for i in xrange(M):
      img[zero[0]][i] = 0
    for j in xrange(N):
      img[j][zero[1]] = 0
  return img

