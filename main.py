#!/usr/bin/env python3
import sys
sys.path.append('./alg/')

from time import time
from random import randint
import quick_select
import numpy as np
#from 1_quick_select.py import *

def test_quick_select():
    # O(n), 1000 2000 4000 8000
    length = [1000,2000,4000,8000]
    # different length find kth x 100 loops
    rs = []
    for each_length in length:
        t_total = 0
        for i in range(1000):
            # prepare
            arr = np.random.rand(each_length)
            k = randint(1, each_length)
            
            # test & count
            t = time()
            quick_select.quick_select(k, arr)
            t_total += (time() - t)
        print('current array length: ',each_length, '1000 loops total time: ',t_total)

if __name__ == '__main__':
    test_quick_select()