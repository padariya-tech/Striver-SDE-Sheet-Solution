class Queue:

    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self, x):
        # Move everything from s1 to s2
        while self.s1:
            self.s2.append(self.s1.pop())

        # Add new element
        self.s1.append(x)

        # Move everything back
        while self.s2:
            self.s1.append(self.s2.pop())

    def pop(self):
        if not self.s1:
            return None

        return self.s1.pop()

    def peek(self):
        if not self.s1:
            return None

        return self.s1[-1]

    def isEmpty(self):
        return len(self.s1) == 0
    
#########################################################

class Queue:

    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self, x):
        self.s1.append(x)

    def pop(self):
        if not self.s1:
            return None

        # Move everything to s2
        while self.s1:
            self.s2.append(self.s1.pop())

        # Remove front element
        ans = self.s2.pop()

        # Move everything back
        while self.s2:
            self.s1.append(self.s2.pop())

        return ans

    def peek(self):
        if not self.s1:
            return None

        while self.s1:
            self.s2.append(self.s1.pop())

        ans = self.s2[-1]

        while self.s2:
            self.s1.append(self.s2.pop())

        return ans

    def isEmpty(self):
        return len(self.s1) == 0