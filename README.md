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

10. k_way_mergesort.py 
O(nlogk)
The first difficulty is uncertain parameters for merging progress. The second difficulty is the merging progress. For the first difficulty, it can be solved with star symbol(* Parameters). Then we can use merge method from heapq package for solving the second difficulty.

11. k_smallest.py
O(nlogk) when n >> k, the time complexity is O(n). Find k smallest numbers in a data stream (k << n). Keep a k-length heap. Reverse the sign for finding the biggest number in the k-length small heap. 

*** CHAPTER FIVE: DP 1. Simple ***

12. max_wis.py
O(n)
Maximum Weighted Independent Set: independent set is a set where no two numbers are neighbors in the original list. 
wis(n) = max (wis(n-2)+lst[n], wis(n-1)), and two dummy 0 in front of the list as base case. 

13. num_bsts.py
O(n^2)
Output the number of possible isomeric binary trees under the given number of nodes n. For n=k, fixing the root, then the first possible structure of left is (dic[0]=1), while right is (dic[k-1]), add to the final result of multiplication of left and right. Then calculate when the number of left node is 1 (dic[1]=1), while right is (dic[k-2]), add to the final result of multiplication of left and right. Get the total summation of when the results when the number of left nodes from 0 to k-1. Return dic[k].

14. num_bits.py
O(n)
Number of bit strings of length n that has
a. no two consecutive 0s.
b. two consecutive 0s.
The sub-problem is quite similar to Fibonacci sequence. Just the problem are not same. 

*** CHAPTER SIX: DP 2. Knapsack ***

15. unbounded.py
O(nW)
Given total weight W and a list of serveral different knapsacks (length is n). Each knapsack has a (weight, value). The problem is to find the maximal value under the given W. Unbounded means ANY knapsacks can be chosen anytimes. The fisrt subproblem is what is the maximal value of each weight (from 1 to W). The second subproblem is what is the  value of choosing each knapsack at each weight. 

16. bounded.py (can be done with a better backtrack)
O(nW'), ' denotes to average count times
The different between bounded and unbounded knapsack problem is there is number of limitation of choosing each knapsacks (w_i, v_i, c_i). The time complexity is O(wn'), w is the total weight, n is the number of bags, ' denotes to the time of counting each number of the same bag under the same weight. The memory should memorize [(weight, # of bag)] for non-repeatly counting using each bag. There are three loops. First, iteratively increase the number of weight. Second, iteratively increase the number of bag. (These two steps as similar as unbounded knapsack problem. ) Last, iteratively increase the times of using same bag. Because we are alwasy choosing the result from last row (i-1) where we doesn't use any currents bag at current row (i). And we exhaustedly counting all possiblites of current bag (from 0 to c_i). Thus, we won't use the bag over the number of it. Hence, the space complexity is O(wn).

17. 01.py 
O(nW)
The different between 01 and bounded knapsack problem is each knapsack only can be chosen at most ONCE. 01 knapsack could be treated as a special case of bounded knapsack when the count of each item is 1. 

*** CHAPTER SEVEN: DP 3. Graph Algorithm ***

18. lis.py
O(n^2)
The problem of the longest increasing sequence(lis). Assume a string sequence (e.g.'zadbc'), the longest increasing sequence is 'abc'. From the perspective of bottom-up, the outter loop (opt[i]) is increasing the length of sequence. The inner sequence (opt[j]) is searching the relationship between each previous sub-sequence and the new element. If the last character of previous sub-sequence less than new element and the lis of previous sequence (opt[j]) + the length of new element (1) is longer than current length (opt[i]). So,
if string[j] < string[i] and opt[j] + 1 > opt[i]: then update current choice.

19. topological.py
O(V+E)
Tranfer a direct graph to a topological order. Push 0 in degree into a FIFO queue. Pop one elem from FIFO queue and add to order and substract degree of connected nodes. At the end, if there would be some nodes left, then there must be a cycle in the graph. Ortherwise, return the order.

20. viterbi.py
O(VE)
This algorithm can solve all similar longest DAG problem (LIS, TSP, knapsacks, MIS). In this problem, it outputs (l,p) where l is the length of the longest path and p denots the path. First, add a dummy sink node. Then with following the increasing topological order (as well as the weight in knapsack problem), using exsited previous nodes to update current nodes. This algorithm is a general solution to any longest problem. 

*** CHAPTER EIGHT: DP 4. Graph Algorithm 2 ***

21. dijkstra.py
O((V+E)logV)    
In this problem, is to find the shortest path from source(0) to sink node(n-1). The requirment of using dijkstra is non-negative path in the graph. The key of solving it is applying heap queue. First push the source node into the heap, then pop it and heap push its connected nodes into heap with their weights. As long as popping the sink node, then the algorithm would return optimal path length. Otherwise, there won't be solution due to the unreachable sink node. 

22. tsp.py (unfinished)
O(2^n) - Exausted method consume O(n!) -

*** CHAPTER NINE: DP 5. RNA structure prediction ***
A-U, C-G, U-G
e.g. ACAGU is a RNA sequence. 
a. best (s): Get the maximal number of pairs is (2, '((.))'). 
b. total (s): Get the number of possible structures (6). 
c. kbest (s, k): Get the k-best structures from 1-th to k-th best. 
Solution:
a. O(n^3)
Using three loops. The first loop is an increased moving "ruler". The second loop move the ruler from leftmost to rightmost. Last the innermost loop search the relationship between the first element and the rest elements and update the BEST memorization. 
b. O(n^3)
Similar to a. The difference between a. and b. is using sum to replace max operation. Besides, the base case is also slightly different (both of them depend on their own meaning). 
c. (unfinished)





