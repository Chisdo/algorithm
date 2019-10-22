# algorithm
ALL descriptions of algorithms are from Prof. Huang's algorithm class projects in OSU in 2018, all implementations are coded by Jiaxin Li. 
./main.py:          shows a few running time results of algorithms
./alg/xxx.py:       implementations of algorithms
./alg/pdf/xxx.pdf:  detailed descriptions of algorithms

*** CHAPTER ONE: quick sort, BST, quick select ***

1. quick_select.py: 
O(n)
Choosing kth smallest number from the array.

2. quick_sort_tree.py:
a. genereate binary search tree with using quick sort algorihtm 
b. decode binary search tree to a list
c. search and insert operation implementation

*** CHAPTER TWO: Divid n Conquer ***

3. merge_sort.py
O(nlogn)
Sort the array with using merge sort algorithm. 

4. num_inversions.py
O(nlogn)
Counting the number of inversed letters in an array. (Similar algorithm to merge sort.)

5. longest_path.py
O(n)
Find the longest path of a tree. Empty tree is 0. A tree like [[[],1,[]], 2, [[],3,[]]] is 2 (1->2->3). The depth of a node = max depth of (left, right). The longest path is equal to the max(left path, right path, current path=left depth + right depth)

*** CHAPTER THREE: K closest number, two pointers ***

6. closest_unsorted.py
O(n)
Find k numbers which are closest to a query number x in the unsorted array. The variety of quick select. First, scan and get distance of all numbers. Then quick select. Last, scan again and find the smaller number. 

7. closest_sorted.py
O(logn + k)
Find k numbers which are closest to a query number x in the sorted array. First, binary search. Then, use pointer to locate the place. 

*** MY WORK: A BETTER SOLUTION ***

(Implemented in: better_closest_sorted(arr, x, k)):
O(logn + logk)
Instead of finding k gradually, we could find k with using binary search. The problem is there would be a lot of boundary check problems. With a larger k, this better solution is much faster than the original algorithm proposed in class.

8. find_triples.py
O(n^2)
Find all triples from an array which only includes distinct number. First, sort the array with O(nlogn). Then create a set for checking if the summation result is in the array. Last, use two loops for iteratively calculate the summation with O(n^2) (n(n-1)/2). 

*** CHAPTER FOUR: priority queue and heaps ***

9. get_smallest_pairs.py
Problem: two arrays which have same length. Then find the smallest n pairs in the Cartesian product of array A and array B. n is the length of A (as well as the length of B). 
O(n^2logn)
a. Sort A,B with O(nlogn). Enumerate c with all elements in the Cartesian product results O(n^2). Then sort the result O(n^2logn). Last find the smallest n pairs. 
O(n^2)
b. Instead of sorting the whole Cartesian results, find the n smallest pairs as threshold O(n^2). Then iterating the result and use threshold to find n smallest pairs O(n^2). 
O(nlogn)
c. A USED set, a HEAP and a result LIST. Fisrt add the (0,0) position element to the heap. Then pop the smallest element from the heap. Add result to the list and used set. Then add (x+1,y) and (x,y+1) elements to the heap. Repeat the loop until the length of list reach the requirment. 

10. k_way_mergesort.py (unfinished)

11. k_smallest.py
O(nlogk) when n >> k, the time complexity is O(n). Find k smallest numbers in a data stream (k << n). Keep a k-length heap. Reverse the sign for finding the biggest number in the k-length small heap. 

*** DP 1 ***

12. max_wis.py
O(n)
Maximum Weighted Independent Set: independent set is a set where no two numbers are neighbors in the original list.



