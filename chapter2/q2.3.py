#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Implement an algorithm to delete a node in the middle of a single linked list,
# given only access to that node.

# example:
# Input: the node 'c' from the linked list a->b->c->d->e->None
# Result: a->b->d->e->None

from LinkedList import Node

v = Node(value=1, next=Node(value=2, next=Node(value=3, next=Node(value=4,
    next=Node(value=5, next=Node(value=6))))))

def delThisNode(node):  
  node.value = node.next.value
  aux = node.next
  node.next = aux.next
  del aux

nodeToDelete = v.next.next.next

v.printAll()
delThisNode(nodeToDelete)
v.printAll()
