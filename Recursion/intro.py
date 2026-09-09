# Recursion => when a function calls it self
#  until a specified condition is met. 

# stack overflow ==> size of the stack is full


n = 10

sum = 0
i = 0
def sumation(i,n):
    print(i)
    if i > n:
        print(i,n)
        return 0
    
    return i + sumation(i+1,n)



print(sumation(0,n))