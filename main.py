#!/usr/bin/env python3
import sys
sys.path.append('./alg/')
sys.path.append('./alg/chapter1')
sys.path.append('./alg/chapter2')
sys.path.append('./alg/chapter3')
sys.path.append('./alg/chapter4')
sys.path.append('./alg/chapter5')
#sys.path.append('./alg/chapter6')
sys.setrecursionlimit(100000)
    
from time import time
from random import randint, shuffle
import numpy as np
import quick_select
import merge_sort
import num_inversions
import closest_sorted


def test_quick_select():
    # O(n), 1000 2000 4000 8000
    length = [1000,2000,3000,4000,5000]
    loops = 1000
    # different length find kth x 1000 loops
    rs = []
    for each_length in length:
        t_total = 0
        for i in range(loops):
            # prepare
            arr = np.random.rand(each_length)
            k = randint(1, each_length)
            
            # test & count
            t = time()
            quick_select.quick_select(k, arr)
            t_total += (time() - t)
        print('current array length: ',each_length,';',  loops, 'loops total time: ',t_total)
        rs.append(t_total)
    return length, rs

def test_merge_sort():
    # O(n), 1000 2000 4000 8000
    length = [1000*i for i in range(1,6)]
    loops = 100
    # different length find kth x 100 loops
    rs = []
    for each_length in length:
        t_total = 0
        for i in range(loops):
            # prepare
            arr = list(range(each_length))
            shuffle(arr)
            # test & count
            t = time()
            merge_sort.merge_sort(arr)
            t_total += (time() - t)
        print('current array length: ',each_length,';', loops, 'loops total time: ',t_total)
        rs.append(t_total)
    return length, rs

def test_num_inversions():
    # O(n), 1000 2000 4000 8000
    length = [1000*i for i in range(1,6)]
    loops = 100
    # different length find kth x 100 loops
    rs = []
    for each_length in length:
        t_total = 0
        for i in range(loops):
            # prepare
            arr = list(range(each_length))
            shuffle(arr)
            # test & count
            t = time()
            num_inversions.num_inversions(arr)
            t_total += (time() - t)
        print('current array length: ',each_length,';', loops, 'loops total time: ',t_total)
        rs.append(t_total)
    return length, rs

def test_closest_sorted():
    # O(n), 1000 2000 4000 8000
    length = [100000*i for i in range(1,6)]
    loops = 10
    k = 10000
    # different length find kth x 100 loops
    rs = []
    for each_length in length:
        t_total1 = 0
        t_total2 = 0
        
        for i in range(loops):
            # prepare
            arr = list(range(each_length))
            shuffle(arr)
            x = randint(5,each_length-5)
            # test & count
            t = time()
            closest_sorted.closest_sorted(arr, x, k)
            t_total1 += (time() - t)

            t = time()
            closest_sorted.better_closest_sorted(arr, x, k)
            t_total2 += (time() - t)
            
        print('current array length: %d; %d loops total time: %f/%f with k: %d' %(each_length, loops, t_total1,  t_total2, k))
        rs.append(t_total1-t_total2)
    return length, rs

if __name__ == '__main__':
    x, y = test_closest_sorted()
    