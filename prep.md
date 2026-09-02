# 100 LeetCode Problems — SDE-2 DSA Preparation

## Goal

- 100 carefully selected problems
- 3 problems per day
- 2 hours per day
- First pass: ~34 days
- Second pass: ~15–20 days
- Focus on pattern recognition rather than problem count
- Goal: Build enough DSA intuition to approach unfamiliar interview problems systematically

---

## 1. Arrays, Hashing & Prefix Sum

1. Two Sum — Hash Map — Easy
2. Contains Duplicate — Hash Set — Easy
3. Valid Anagram — Frequency Map — Easy
4. Group Anagrams — Hashing / Canonical Representation — Medium
5. Top K Frequent Elements — Hash Map + Heap/Bucket — Medium
6. Product of Array Except Self — Prefix/Suffix — Medium
7. Longest Consecutive Sequence — Hash Set — Medium
8. Subarray Sum Equals K — Prefix Sum + Hash Map — Medium

### Patterns to Learn

- Hash Map
- Hash Set
- Frequency Counting
- Prefix/Suffix
- Prefix Sum
- Prefix Sum + Hash Map
- Canonical Representation

---

## 2. Two Pointers

9. Valid Palindrome — Opposing Pointers — Easy
10. Two Sum II - Input Array Is Sorted — Two Pointers — Medium
11. 3Sum — Sort + Two Pointers — Medium
12. Container With Most Water — Greedy Two Pointers — Medium
13. Trapping Rain Water — Two Pointers / Prefix Maxima — Hard

### Patterns to Learn

- Left/Right Pointers
- Sorted Array Two-Pointer Search
- Fix One Element + Two Pointers
- Greedy Pointer Movement
- Maintaining Left/Right Maximums

---

## 3. Sliding Window

14. Best Time to Buy and Sell Stock — Running Minimum — Easy
15. Longest Substring Without Repeating Characters — Variable Window — Medium
16. Longest Repeating Character Replacement — Window + Frequency — Medium
17. Permutation in String — Fixed-Size Window — Medium
18. Minimum Window Substring — Variable Window + Counts — Hard
19. Sliding Window Maximum — Monotonic Deque — Hard

### Patterns to Learn

- Fixed-Size Sliding Window
- Variable-Size Sliding Window
- Expand Right
- Shrink Left
- Frequency Maps Inside Windows
- Maintaining Window Invariants
- Monotonic Deque

---

## 4. Stack & Monotonic Stack

20. Valid Parentheses — Stack — Easy
21. Min Stack — Auxiliary State — Medium
22. Evaluate Reverse Polish Notation — Stack — Medium
23. Daily Temperatures — Monotonic Stack — Medium
24. Car Fleet — Sort + Stack Reasoning — Medium
25. Largest Rectangle in Histogram — Monotonic Stack — Hard

### Patterns to Learn

- LIFO Processing
- Stack-Based Parsing
- Maintaining Auxiliary State
- Next Greater Element
- Next Smaller Element
- Monotonic Increasing Stack
- Monotonic Decreasing Stack
- Boundary Calculation

---

## 5. Binary Search

26. Binary Search — Basic Binary Search — Easy
27. Search a 2D Matrix — Search-Space Reduction — Medium
28. Koko Eating Bananas — Binary Search on Answer — Medium
29. Find Minimum in Rotated Sorted Array — Modified Binary Search — Medium
30. Search in Rotated Sorted Array — Modified Binary Search — Medium
31. Time Based Key-Value Store — Binary Search — Medium
32. Median of Two Sorted Arrays — Partition Binary Search — Hard

### Patterns to Learn

- Standard Binary Search
- Lower/Upper Bound
- Rotated Sorted Arrays
- Binary Search on Answer
- Monotonic Search Spaces
- Partition-Based Binary Search

---

## 6. Linked Lists

33. Reverse Linked List — Pointer Manipulation — Easy
34. Merge Two Sorted Lists — Merge — Easy
35. Linked List Cycle — Fast/Slow Pointers — Easy
36. Reorder List — Split + Reverse + Merge — Medium
37. Remove Nth Node From End of List — Fast/Slow Pointers — Medium
38. Copy List with Random Pointer — Mapping / Interweaving — Medium
39. Add Two Numbers — Simulation — Medium
40. LRU Cache — Hash Map + Doubly Linked List — Medium

### Patterns to Learn

- Pointer Manipulation
- Dummy Nodes
- Fast/Slow Pointers
- Linked-List Reversal
- Finding Midpoint
- Merging Lists
- Hash Map + Doubly Linked List

---

## 7. Trees & BST

41. Invert Binary Tree — Tree Recursion — Easy
42. Maximum Depth of Binary Tree — DFS/BFS — Easy
43. Diameter of Binary Tree — Postorder DFS — Easy
44. Balanced Binary Tree — Bottom-Up DFS — Easy
45. Same Tree — Recursive Comparison — Easy
46. Subtree of Another Tree — Tree Matching — Easy
47. Binary Tree Level Order Traversal — BFS — Medium
48. Binary Tree Right Side View — BFS/DFS — Medium
49. Count Good Nodes in Binary Tree — DFS + Path State — Medium
50. Validate Binary Search Tree — Bounds / Inorder — Medium
51. Kth Smallest Element in a BST — Inorder Traversal — Medium
52. Construct Binary Tree from Preorder and Inorder Traversal — Recursion + Indexing — Medium
53. Binary Tree Maximum Path Sum — Tree DP — Hard
54. Serialize and Deserialize Binary Tree — Tree Encoding — Hard

### Patterns to Learn

- DFS
- BFS
- Preorder
- Inorder
- Postorder
- Top-Down Recursion
- Bottom-Up Recursion
- Passing State Downward
- Returning Information Upward
- BST Invariants
- Tree Construction
- Tree DP

---

## 8. Heap & Priority Queue

55. Kth Largest Element in an Array — Heap / Quickselect — Medium
56. K Closest Points to Origin — Heap — Medium
57. Task Scheduler — Heap / Greedy — Medium
58. Find Median from Data Stream — Two Heaps — Hard

### Patterns to Learn

- Min Heap
- Max Heap
- Top-K Problems
- Heap of Size K
- Scheduling Using Heaps
- Two-Heap Median Pattern
- Quickselect

---

## 9. Intervals & Greedy

59. Merge Intervals — Sort + Sweep — Medium
60. Insert Interval — Interval Manipulation — Medium
61. Non-overlapping Intervals — Greedy — Medium
62. Meeting Rooms II — Sweep Line / Heap — Medium
63. Jump Game — Greedy Reachability — Medium
64. Jump Game II — Greedy BFS-Style Ranges — Medium
65. Gas Station — Greedy Invariant — Medium

### Patterns to Learn

- Sorting Intervals
- Interval Merging
- Overlap Detection
- Sweep Line
- Greedy Selection
- Greedy Reachability
- Proving Greedy Invariants

---

## 10. Backtracking

66. Subsets — Decision Tree — Medium
67. Combination Sum — Backtracking — Medium
68. Permutations — Backtracking — Medium
69. Subsets II — Duplicates + Backtracking — Medium
70. Combination Sum II — Duplicates + Pruning — Medium
71. Word Search — Grid Backtracking — Medium
72. Palindrome Partitioning — Backtracking — Medium
73. N-Queens — Constraint Backtracking — Hard

### Patterns to Learn

- Decision Trees
- Choose
- Explore
- Undo
- State Restoration
- Duplicate Elimination
- Pruning
- Grid Backtracking
- Constraint Tracking

---

## 11. Graphs

74. Number of Islands — Grid DFS/BFS — Medium
75. Clone Graph — Graph Traversal + Map — Medium
76. Max Area of Island — DFS/BFS — Medium
77. Rotting Oranges — Multi-Source BFS — Medium
78. Pacific Atlantic Water Flow — Reverse Graph Traversal — Medium
79. Surrounded Regions — Boundary Traversal — Medium
80. Course Schedule — Cycle Detection / Topological Sort — Medium
81. Course Schedule II — Topological Sorting — Medium
82. Graph Valid Tree — DFS / Union-Find — Medium
83. Number of Connected Components in an Undirected Graph — Union-Find / DFS — Medium
84. Word Ladder — BFS — Hard

### Patterns to Learn

- Adjacency Lists
- DFS
- BFS
- Grid-as-Graph
- Connected Components
- Multi-Source BFS
- Cycle Detection
- Topological Sorting
- Kahn's Algorithm
- Union-Find
- Shortest Path in Unweighted Graphs

---

## 12. Advanced Graph Algorithms

85. Network Delay Time — Dijkstra — Medium
86. Min Cost to Connect All Points — Minimum Spanning Tree — Medium
87. Cheapest Flights Within K Stops — Shortest Path / Bellman-Ford — Medium
88. Alien Dictionary — Topological Sorting — Hard

### Patterns to Learn

- Weighted Graphs
- Dijkstra's Algorithm
- Bellman-Ford
- Minimum Spanning Tree
- Prim's Algorithm
- Kruskal's Algorithm
- Graph Construction from Implicit Relationships

---

## 13. 1-D Dynamic Programming

89. Climbing Stairs — Basic DP — Easy
90. House Robber — State Transition — Medium
91. House Robber II — Circular DP — Medium
92. Coin Change — Unbounded Knapsack — Medium
93. Longest Increasing Subsequence — DP / Binary Search — Medium
94. Word Break — Prefix DP — Medium
95. Partition Equal Subset Sum — 0/1 Knapsack — Medium

### Patterns to Learn

- Defining DP State
- Recurrence Relations
- Memoization
- Tabulation
- Space Optimization
- Take/Not-Take Decisions
- 0/1 Knapsack
- Unbounded Knapsack
- Prefix DP

---

## 14. 2-D & Sequence Dynamic Programming

96. Unique Paths — Grid DP — Medium
97. Longest Common Subsequence — 2-D DP — Medium
98. Coin Change II — Knapsack DP — Medium
99. Edit Distance — Sequence DP — Medium
100. Longest Palindromic Subsequence — Interval / Sequence DP — Medium

### Patterns to Learn

- 2-D State Representation
- Grid DP
- Sequence Comparison
- Include/Exclude Transitions
- DP Over Two Strings
- Interval DP
- Space Optimization

---

# Daily Schedule

Target: **3 problems per day**

Total time: **~2 hours**

```text
Problem 1    35 min
Problem 2    35 min
Problem 3    35 min
Review       15 min
------------------
Total       120 min
```

Do not force three problems if one is particularly difficult.

A Hard problem can count as two problem slots.

---

# Problem-Solving Protocol

For every problem, follow the same process.

## Step 1 — Understand

Identify:

- Input
- Output
- Constraints
- Edge cases

Ask:

> What is the brute-force solution?

---

## Step 2 — Derive Brute Force

Do not immediately jump to the optimal solution.

Understand:

- What work is being repeated?
- What makes the brute-force solution slow?
- What is the complexity?
- Which operation is the bottleneck?

---

## Step 3 — Identify the Pattern

Ask whether the problem resembles:

- Hashing
- Prefix Sum
- Two Pointers
- Sliding Window
- Stack
- Monotonic Stack
- Binary Search
- Linked List
- Tree DFS/BFS
- Heap
- Intervals
- Greedy
- Backtracking
- Graph DFS/BFS
- Topological Sort
- Union-Find
- Shortest Path
- Dynamic Programming

---

## Step 4 — Define the Invariant

Before coding, answer:

> What remains true throughout the algorithm?

Examples:

### Sliding Window

> The current window contains no duplicate characters.

### Binary Search

> The answer always remains inside the current search space.

### BST

> Every node must fall inside the valid range inherited from its ancestors.

### Dynamic Programming

> `dp[i]` represents the optimal answer for the first `i` elements.

---

## Step 5 — Implement

Write the solution without referring to another implementation.

Focus on:

- Correctness
- Clean variable names
- Boundary conditions
- Minimal unnecessary state

---

## Step 6 — Complexity Analysis

Always explicitly calculate:

```text
Time Complexity: O(?)
Space Complexity: O(?)
```

Do not simply memorize complexity.

Understand where it comes from.

---

## Step 7 — Explain the Solution

After solving, explain the algorithm verbally as if this were an interview.

You should be able to explain:

1. Brute-force approach
2. Why brute force is inefficient
3. Key observation
4. Optimal algorithm
5. Why the algorithm is correct
6. Time complexity
7. Space complexity

---

# The 20 Core Patterns to Internalize

By the end of these 100 problems, you should be comfortable with:

1. Hash Map / Hash Set
2. Prefix Sum
3. Two Pointers
4. Sliding Window
5. Stack
6. Monotonic Stack
7. Binary Search
8. Binary Search on Answer
9. Fast/Slow Pointers
10. Tree DFS
11. Tree BFS
12. Heap / Priority Queue
13. Intervals
14. Greedy
15. Backtracking
16. Graph DFS/BFS
17. Topological Sort
18. Union-Find
19. Shortest Path / MST
20. Dynamic Programming

The goal is **not**:

> I solved 100 LeetCode problems.

The goal is:

> I can identify which family an unfamiliar problem belongs to and derive the solution from the underlying pattern.

---

# First Pass — ~34 Days

Solve all 100 problems.

Do not expect perfect retention.

Mark every problem:

```text
GREEN  = Solved independently and understood clearly
YELLOW = Solved but needed hints / struggled
RED    = Could not independently derive the solution
```

A reasonable result after the first pass:

```text
GREEN   ~40–60
YELLOW  ~25–40
RED     ~10–20
```

The exact numbers do not matter.

The classification tells you what needs repetition.

---

# Second Pass — ~15–20 Days

Do **not** automatically redo all 100.

Redo:

- Every RED
- Most YELLOW
- Important GREEN problems whose patterns you have forgotten

Target approximately **40–50 problems**.

Do them without looking at your previous solution.

The objective is **retrieval**, not recognition.

Seeing a solution and thinking:

> I remember this.

is not sufficient.

You need to be able to reconstruct the algorithm independently.

---

# Pattern Recognition Test

After the second pass, start solving unfamiliar problems.

Give yourself 3–5 minutes before coding.

Ask:

1. What category is this?
2. What pattern probably applies?
3. What invariant should I maintain?
4. What data structure makes the operations efficient?
5. What should the expected complexity be?

---

## Recognition Examples

### "Longest substring satisfying X"

Think:

```text
Sliding Window
```

### "Minimum X such that condition Y becomes possible"

Think:

```text
Binary Search on Answer
```

### "Dependencies between courses/tasks"

Think:

```text
Directed Graph
Topological Sort
Cycle Detection
```

### "Next greater/smaller element"

Think:

```text
Monotonic Stack
```

### "Minimum number of steps in an unweighted graph"

Think:

```text
BFS
```

### "Repeated optimal decision over prefixes"

Think:

```text
Dynamic Programming
```

### "Top K / Kth largest / repeatedly need smallest or largest"

Think:

```text
Heap / Priority Queue
```

### "Connected groups"

Think:

```text
DFS / BFS / Union-Find
```

### "All combinations / arrangements / choices"

Think:

```text
Backtracking
```

### "Sorted input + searching for pair"

Think:

```text
Two Pointers
```

---

# What to Record for Every Problem

Maintain short notes for every problem.

Use this format:

```markdown
## Problem

### Pattern
Sliding Window

### Brute Force
...

### Key Observation
...

### Invariant
...

### Optimal Approach
...

### Time Complexity
O(...)

### Space Complexity
O(...)

### What I Missed
...

### Recognition Trigger
If I see ________, think ________.

### Status
GREEN / YELLOW / RED
```

Keep the notes short.

The purpose is not to document the entire solution.

The purpose is to record **what you learned from the problem**.

---

# Additional Problems After the Core 100

Once the core 100 are complete, add these.

## Trie

101. Implement Trie (Prefix Tree)
102. Design Add and Search Words Data Structure
103. Word Search II

## Bit Manipulation

104. Single Number
105. Number of 1 Bits
106. Counting Bits
107. Reverse Bits
108. Missing Number
109. Sum of Two Integers

## Additional Graph / DP

110. Redundant Connection
111. Swim in Rising Water
112. Burst Balloons
113. Distinct Subsequences
114. Interleaving String

---

# Final Success Criteria

Do not measure progress primarily by the number of solved problems.

After this curriculum, you should be able to look at an unfamiliar problem and reason:

> This looks like a variable sliding-window problem.

> This is binary search over the answer space.

> This recursion needs information returned from the children, so this is bottom-up tree DFS.

> This is shortest path in an unweighted graph, therefore BFS.

> This is a dependency graph, therefore I should investigate topological sorting.

> This is a take/not-take decision with overlapping subproblems, therefore DP.

> This asks for the next larger element, so I should investigate a monotonic stack.

> This repeatedly needs the smallest/largest element, so a heap is probably appropriate.

> This asks me to enumerate choices and undo decisions, so this is backtracking.

---

# Core Principle

**Do not optimize for LeetCode count. Optimize for pattern recognition.**

100 deeply understood problems are substantially more valuable than 300 problems solved by memorizing implementations.

The end goal is for problem #101 to feel like:

> I haven't seen this exact problem before, but I've seen the underlying pattern.