#!/usr/bin/env python
# -*- coding: utf-8 -*-

# You have two numbers represented by a linked list, where each node contains a
# single digit. The digits are stoed in reverse order, such that the 1's digit
# is at the head of the list. Write a function that adds the two numbers and
# returns the sum as a linked list.

# Example
# Input: (3->1->5), (5->9->2)
# Output:(8->0->8)

from LinkedList import Node

n1 = Node(value=3, next=Node(value=1, next=Node(5)))
n2 = Node(value=5, next=Node(value=9, next=Node(2)))

def sumIt(n1, n2, carry):
  if (n1 is None) and (n2 is None):
    return None
  result = Node()
  v = carry
  if n1 is not None:
    v += n1.value
  if n2 is not None:
    v += n2.value
  result.value = v%10
  next = sumIt(n1.next, n2.next, v/10)
  result.next = next
  return result

sumIt(n1, n2, 0).printAll()
