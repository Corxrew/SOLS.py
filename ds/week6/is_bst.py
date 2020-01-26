#!/usr/bin/python3

import sys, threading

sys.setrecursionlimit(10**7) 
threading.stack_size(2**25) 
def IsBinarySearchTree(it, min, max):
  if not it in tree: return True
  if tree[it][0] < min or tree[it][0] > max: return False
  return IsBinarySearchTree(tree[it][1], min, tree[it][0] - 1) and IsBinarySearchTree(tree[it][2], tree[it][0] + 1, max)


def main():
  nodes = int(sys.stdin.readline().strip())
  global tree
  tree, int_max, int_min = {}, 2147483647, -2147483647
  for i in range(nodes):
    tree[i] = (list(map(int, sys.stdin.readline().strip().split())))
  if IsBinarySearchTree(0, int_min, int_max):
    print("CORRECT")
  else:
    print("INCORRECT")
threading.Thread(target = main).start()