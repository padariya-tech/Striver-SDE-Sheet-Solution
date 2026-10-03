class Queue:

    def __init__(self, n):
        self.arr = [None] * n
        self.front = 0
        self.rear = 0

    def push(self, val):

        # Queue is full
        if self.rear == len(self.arr):
            raise ValueError("queue is full")

        self.arr[self.rear] = val
        self.rear += 1

    def pop(self):

        # Queue is empty
        if self.front == self.rear:
            raise ValueError("queue is empty")

        val = self.arr[self.front]

        # Optional: remove reference
        self.arr[self.front] = None

        self.front += 1

        return val

    def top_of_queue(self):

        # Queue is empty
        if self.front == self.rear:
            raise ValueError("queue is empty")

        return self.arr[self.front]

    def size_of_queue(self):

        return self.rear - self.front


if __name__ == "__main__":

    n = 10

    q = Queue(n)

    q.push(1)
    q.push(2)
    q.push(3)
    q.push(4)
    q.push(5)

    print(q.pop())           # 1
    print(q.top_of_queue())  # 2
    print(q.size_of_queue()) # 4