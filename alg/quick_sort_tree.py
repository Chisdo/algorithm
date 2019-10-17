#!/usr/bin/env python3
from random import randint

def sort(arr):
    # time: O(nlogn)
    # return a list of tree [[left], [root], [right]]
    if len(arr) == 0:
        return []
    pivot = arr[0]
    left = [x for x in arr if x < pivot]
    mid = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return [sort(left)] + mid + [sort(right)]
# sorted (tree): return a list
# search (tree, x): return a boolean
# _search (tree, x): return the subtree rooted at x where x is found or [] where x should be inserted
# insert (tree, x): return a NONE

def sorted(tree): # infix traversal
    l,root,r = tree[0]
    return l,root,r
if __name__ == '__main__':
    a = [4,2,6,3,6,7,1,9]
    t = sort(a)
    print(sorted(t)) # expected: [[[[], 1, []], 2, [[], 3, []]], 4, [[], 6, 6, [[], 7, [[], 9, []]]]]
