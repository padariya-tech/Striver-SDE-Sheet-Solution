class Queue:

    def __init__(self,n):
        self.arr = [None] * n
        self.front = 0
        self.rear = 0

    def push(self,val):
        if self.rear == len(self.arr):
            raise ValueError("queue is full")
        
        self.arr[self.rear] = val
        self.rear += 1

    def pop(self):
        if self.front < self.rear:
            raise ValueError("queue is empty")
        val = self.arr[self.front]
        self.front += 1
        return val

    def top_of_queue(self):
        if self.rear < self.front:
            raise ValueError("queue is empty")
        return self.arr[self.front]
    
    def size_of_queue(self):
        if self.rear < self.front:
            raise ValueError("queue is empty")
        return (self.rear - self.front)


if __name__ == "__main__":

    n = 10
    st = Queue(n)
    st.push(1)
    st.push(2)
    st.push(3)
    st.push(4)
    st.push(5)
    print(st.pop())
    print(st.top_of_queue())
    print(st.size_of_queue())
