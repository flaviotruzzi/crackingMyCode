#!/usr/bin/env python

# Given an image represented by an NxN matrix, where each pixel in the image is
# 4 bytes, write a mehtod to rotate the image by 90 degrees. Can you do this in
# place?

from numpy import *
N = 10
img = random.randint(255, size=(N, N)).tolist()

imgr = [[-1 for x in xrange(N)] for y in xrange(N)]
    
def rotate(img, N):
  for layer in xrange(N / 2):
    first = layer
    last = N - 1 - layer
    for i in xrange(first, last):
      offset = i - first
      top = img[first][i] # save top

      # left -> top
      img[first][i] = img[last - offset][first]

      # bottom -> left
      img[last - offset][first] = img[last][last - offset]

      # right -> bottom
      img[last][last - offset] = img[i][last]

      # top -> right
      img[i][last] = top
  return img

def rotate2(img, N):


