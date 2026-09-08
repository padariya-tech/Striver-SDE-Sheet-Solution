# Introduction to Dynamic Programming
# tabulation(bottom-up) and memoization(top-down)
# bottom-up means try to go from 
# base case to required answer 



# overlapping sub problem 
# memoization ==> tend to store the value of sub problems
# in some map / table.

# recursion in tabulation

# base case from to required answer
# initialize the same DP array with same size
# change funciton to dp
# f(n-1) = dp[n-1]
# in tabulation no recursion stack space



# DP hack

# 1) try to represent problem in terms of index
# 2) do all possible stuffs on that index according to 
#     problem statement
# 3) sum of all stuffs => count all ways
#     min of all stuffs => find minimum of all the ways
#     max of all stuffs => find maximum of all the ways