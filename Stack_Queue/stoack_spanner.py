class StockSpanner:
    def __init__(self):
        self.idx = -1
        self.st = []

    def next(self, price: int) -> int:
        
        self.idx += 1
        res = 1
        while self.st and self.st[-1][0] <= price:
            self.st.pop()

        res = self.idx - (self.st[-1][1] if self.st else -1)
        # print(res, self.st, self.idx, price)
        self.st.append((price, self.idx))
        return res


if __name__ == "__main__":
    price = [7,2,1,3,3,1,8]
    obj = StockSpanner()
    
    for i in range(len(price)):
        print(obj.next(price[i]))

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)