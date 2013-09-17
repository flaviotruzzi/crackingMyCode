#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Write code to remove duplicates from an unsorted linked list.
# Follow up: How would you solve this problem is a temporary buffer is not
# allowed?

from LinkedList import Node

v = Node(value='a', next=Node(value='b', next=Node(value='c',
next=Node(value='a', next=Node(value='b', next=Node(value='z'))))))

# using buffer
def removeDuplicates(node):
  buf = set()
  previous = Node()
  while node is not None:
    if node.value in buf:
      previous.next = node.next
    else:
      buf.add(node.value)
      previous = node
    node = node.next

#without buffer
def removeDuplicates2(node):
  previous = node
  current = node.next
  while current is not None:
    aux = node
    while aux is not current:
      if aux.value == current.value:
        tmp = current.next
        previous.next = tmp
        current = tmp
        break
      aux = aux.next
    if aux == current:
      previous = current
      current = current.next


