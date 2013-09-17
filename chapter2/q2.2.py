#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Implement an algorithm to find the nth to last element of a singly linked
# list.

v = Node(value=1, next=Node(value=2, next=Node(value=3, next=Node(value=4,
  next=Node(value=5, next=Node(value=6))))))

# without recursion
def getNth(v, n):
  p1 = v
  p2 = v
  for i in xrange(n-1):
    p2 = p2.next
  if p2.next is None:
    return p1
  while p2.next is not None:
    p1 = p1.next
    p2 = p2.next
  return p1

# with recursion
def getNth2(current, behind, n):
  if n-1 is not 0:
    return getNth2(current.next, behind, n-1)
  elif current.next is None:
    return behind
  return getNth2(current.next, behind.next, n)
