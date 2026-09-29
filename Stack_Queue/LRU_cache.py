class Node:

    def __init__(self,key=0,value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} # map for storing key and loc of ll node

        self.head = Node()
        self.tail = Node()

        self.head.next = self.tail
        self.tail.prev = self.head

    def add(self,node):

        node.next = self.head.next
        self.head.next.prev = node

        self.head.next = node
        node.prev = self.head

    def remove(self,node):

        node.prev.next = node.next
        node.next.prev = node.prev

    def get(self, key: int):

        if key not in self.cache:
            return -1
        
        node = self.cache[key]

        self.remove(node)
        self.add(node)

        return node.value
        

    def put(self, key: int, value: int):

        if key in self.cache:
            node = self.cache[key]

            node.value = value

            self.remove(node)
            self.add(node)

            return
        
        node = Node(key,value)

        self.cache[key] = node
        self.add(node)

        if len(self.cache) > self.capacity:

            lru = self.tail.prev

            self.remove(lru)

            del self.cache[lru.key]
        

if __name__ == "__main__":


    capacity = 4
    obj = LRUCache(capacity)

    obj.put(2,6)
    obj.put(4,7)
    obj.put(8,11)
    obj.put(7,10)
    print(obj.get(2))
    print(obj.get(8))
    obj.put(5,6)
    print(obj.get(7))
    obj.put(5,7)
    print(obj.get(5))


