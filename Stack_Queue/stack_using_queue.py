from collections import deque

class Stack:

    def __init__(self):
        self.q = deque()
        self.size = 0

    def push(self, x):
        self.q.append(x)
        self.size += 1

        # Move all previous elements behind the new element
        for _ in range(1, self.size):
            self.q.append(self.q.popleft())

    def pop(self):
        if self.size == 0:
            return None

        self.size -= 1
        return self.q.popleft()

    def top(self):
        if self.size == 0:
            return None

        return self.q[0]

    def isEmpty(self):
        return self.size == 0