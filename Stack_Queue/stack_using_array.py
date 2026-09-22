class Stack:

    def __init__(self,n):
        self.arr = [None] * n
        self.top = -1

    def push(self,val):
        if self.top == len(self.arr):
            raise ValueError("stack is full")
        self.top += 1
        self.arr[self.top] = val

    def pop(self):
        if self.top == -1:
            raise ValueError("stack is empty")
        val = self.arr[self.top]
        self.top -= 1
        return val

    def top_of_stack(self):
        if self.top == -1:
            raise ValueError("stack is empty")
        return self.arr[self.top]
    
    def size_of_stack(self):
        if self.top == -1:
            raise ValueError("stack is empty")
        return (self.top+1)


if __name__ == "__main__":

    n = 10
    st = Stack(n)
    st.push(1)
    st.push(2)
    st.push(3)
    st.push(4)
    st.push(5)
    print(st.pop())
    print(st.top_of_stack())
    print(st.size_of_stack())
