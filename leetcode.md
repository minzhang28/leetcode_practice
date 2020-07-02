### Leetcode practices

#### Stacks
- [739: Daily Temperatures](https://leetcode.com/problems/daily-temperatures/)
  This is a typical usage of monotone stack, refer to this [video(Chinese)](https://leetcode-cn.com/problems/daily-temperatures/solution/leetcode-tu-jie-739mei-ri-wen-du-by-misterbooo/) or this [Medium post (English)](https://medium.com/@vishnuvardhan623/monotonic-stack-e9dcc4fa8c3e) for details

- [503: Next Greater Element II](https://leetcode.com/problems/next-greater-element-ii/)
  This is VERY similar to 739

- [394. Decode String](https://leetcode.com/problems/decode-string/)


#### Two pointers
two pointers are mostly used in sorted array / string, or to optimized the BigO from O(n2) to O(n). 

- [392 is substring](https://leetcode.com/problems/is-subsequence/)
- [88. Merge Sorted Array](https://leetcode.com/problems/merge-sorted-array/)  
- [792.Number of Matching Subsequences](https://leetcode.com/problems/number-of-matching-subsequences/)

#### Array
- [238. Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/):
    Pay attention on the solution on this question, it's a typical solution for this kind of problems
- [27.remove element]()
   Two pointer is used very often in array, please pay attention. normally have a faster pointer and a slow pointer, we can control it to O(n)

#### Tree
- [144. Binary Tree Preorder Traversal](https://leetcode.com/problems/binary-tree-preorder-traversal/)
- [94: Binary Tree Inorder Traversal](https://leetcode.com/problems/binary-tree-inorder-traversal/)
- [145: Binary Tree postorder Traversal ](https://leetcode.com/problems/binary-tree-postorder-traversal/)


### Sorting
#### Binary Sort
  - [153: find-minimum-in-rotated-sorted-array](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/)
     two ways of solving this issue:
     - O(n): set a variable `min_val`, loop the array, and eventually get the min min_val
     - O(log n): using binary sort, this is a typical question to use binary sort, similar as question 154
  typical questions for Binary sorts are
  - 33
  - 34
  - 154

#### [Nation Flag issue](https://en.wikipedia.org/wiki/Dutch_national_flag_problem)
- [s.Chinese explaination](https://mp.weixin.qq.com/s/YcLtbLK_D2V5iQkN5MD0Vg)
- [75 sort colors](https://leetcode.com/problems/sort-colors/)

#### Merge Sort
- [148. Sort List](https://leetcode.com/problems/sort-list/)
