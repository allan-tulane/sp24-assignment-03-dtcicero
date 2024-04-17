# CMPS 2200 Assignment 3
## Answers

**Name:** Daniel Cicero


Place all written answers from `assignment-03.md` here for easier grading.

1a. Start by selecting the highest denomination coin possible, 2^k, such that 2^k <= N. Then, subtract 2^k from N. Finally, repeat steps 1 and 2 until N = 0.

1b. Greedy Choice: The greedy choice property holds that always choosing the locally optimal solution will necessarily lead to the overall optimal solution. In this case, at each step the greedy choice is made by choosing the highest denomination coin possible (maximizing the value of k) as to minimize the number of coins needed. 

Optimal Substructure: This property holds that the optimal solution contains optimal solutions to contained subproblems. In this case, we can look at the remaining value N after choosing the highest denomination coin 2^k. Finding the optimal solution for this new N is equivalent so the optimal solution for the greater problem, proving its optimal substructure. 

1c. Work: O(log n)
    Span: O(1)


2a. Suppose the available denominations in Fortuito are as follows: D1 = $1, D2 = $3, and D3 = $4. In this case, suppose N = 6. Using my algorithm above, we would choose D3 = $4 first, as it is the largest available value <= N. We would then be forced to choose D1 = $1 twice, for a total of 3 coins: {D3, D1, D1}. However, the optimal solution in Fortuito would be to simply choose D2 = $3 twice: {D2, D2}. Therefore, my solution above is not always optimal in Fortuito.

2b. This problem exhibits optimal substructure for the same reason as does problem 1, which is that optimal solutions for subproblems within the greater problem can be constructed from the solution of the greater problem. For instance, in the process of solving the fewest coins for any N, we also contain in that solution the answer to fewest coins for any N', so long as 0 <= N' <= N. Therefore, optimal substructure is proven.

2c. 1. Create a boolean array 'possible' of size N+1. Initialize all values to False.
2. Set possible[0] to True, as it is always possible to make change for $0.
3. For each denomination D:
      For each amount i from 0 to N - D:
        If possible[i] is True, set possible[i + D] to True
   If possible[N] is True, it is possible to make change for N.

   Work: O(N)
   Span: O(N)
