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
    if tree[0] == [] and tree[2] == []:
        return [tree[1]]

    l,root,r = tree
    if l == [] and r != []:
        return [root]+ sorted(r)
    elif l != [] and r == []:
        return sorted(l) + [root]
    else: # l != [] and r != []
        return sorted(l) + [root] + sorted(r)

def _search(tree, x):
    if tree == []:
        return tree
    if tree[1] == x:
        return tree
    if tree[1] < x:
        return _search(tree[2], x)
    if tree[1] > x:
        return _search(tree[0], x)

def search(tree, x):
    place = _search(tree, x)
    if place == []:
        return False
    if place != []:
        return True

def insert(tree, x):
    place = _search(tree, x)
    if place == []:
        place += [[], x, []] # '[]+sth' means add 'sth' on '[]' position
    
if __name__ == '__main__':
    a = [4,2,6,3,5,7,1,9]
    t = sort(a)
    
    print(t)
    print(sorted(t)) # expected: [[[[], 1, []], 2, [[], 3, []]], 4, [[], 6, 6, [[], 7, [[], 9, []]]]]
    print(search(t, 6)) # expected: True
    print(search(t, 6.5)) # expected: False
    insert(t, 6.5) # expected: 
    print(t)
    insert(t, 3)
    print(t)
    
    print(_search(t, 3)) # expected: [[],3,[]]
    print(_search(t, 0) is _search(t, 6.5)) # expected: False
    print(_search(t, 0) == _search(t, 6.5)) # expected: True, value are same while address are not same
    