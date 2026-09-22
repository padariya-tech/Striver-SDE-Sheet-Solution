class MinStack:

    def __init__(self):
        self.st = []
        self.min_val = float('inf')

    def push(self, x):
        if not self.st:
            self.st.append(x)
            self.min_val = x

        elif x < self.min_val:
            # Encode the previous minimum instead of storing in variable
            self.st.append(2 * x - self.min_val)
            self.min_val = x

        else:
            self.st.append(x)

    def pop(self):
        if not self.st:
            return None

        top = self.st.pop()

        # Encoded value
        if top < self.min_val:
            actual_value = self.min_val

            # Restore previous minimum
            self.min_val = 2 * self.min_val - top

            return actual_value

    # Normal value
        return top
    
    def top(self):
        if not self.st:
            return None

        top = self.st[-1]

        if top < self.min_val:
            # Decode actual value
            return self.min_val

        return top

    def getMin(self):
        if not self.st:
            return None

        return self.min_val