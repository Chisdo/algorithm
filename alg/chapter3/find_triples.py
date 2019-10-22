#!/usr/bin/env python3
from random import randint

def find_triples(arr):
    # O(n^2)
    # O(nlogn) for sorting
    arr.sort()

    # creating the set
    numbers = set()
    for elem in arr:
        numbers.add(elem)
    # O(n^2) for iterating with two loops
    rs = []
    for i in range(len(arr)-1):
        for j in range(i+1, len(arr)):
            if arr[i] + arr[j] in numbers:
                rs.append((arr[i],arr[j],arr[i] + arr[j]))
    return rs

if __name__ == '__main__':
    print(find_triples([1,4,2,3,5])) # [(1,3,4),(1,2,3),(1,4,5),(2,3,5)]
    