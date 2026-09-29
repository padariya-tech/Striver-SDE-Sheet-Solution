class Node:

    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):

        self.capacity = capacity

        # HashMap:
        # key -> corresponding Node in the doubly linked list
        # This allows O(1) lookup of a key.
        self.cache = {}

        # Dummy head and tail nodes
        #
        # Structure:
        # HEAD <-> Node <-> Node <-> TAIL
        #
        # Head side = Most Recently Used (MRU)
        # Tail side = Least Recently Used (LRU)
        self.head = Node()
        self.tail = Node()

        self.head.next = self.tail
        self.tail.prev = self.head

    def add(self, node):

        # Add node immediately after HEAD.
        # Therefore, this node becomes the
        # Most Recently Used node.

        node.next = self.head.next
        self.head.next.prev = node

        self.head.next = node
        node.prev = self.head

    def remove(self, node):

        # Remove node from its current position.
        #
        # Example:
        #
        # A <-> Node <-> B
        #
        # becomes:
        #
        # A <-> B

        node.prev.next = node.next
        node.next.prev = node.prev

    def get(self, key: int):

        # Key does not exist
        if key not in self.cache:
            return -1

        # Get the node from HashMap
        node = self.cache[key]

        # Since this key was accessed,
        # it becomes the Most Recently Used node.
        #
        # First remove it from its old position
        # and then add it after HEAD.
        self.remove(node)
        self.add(node)

        return node.value

    def put(self, key: int, value: int):

        # Case 1: Key already exists
        if key in self.cache:

            # Get existing node
            node = self.cache[key]

            # Update its value
            node.value = value

            # Since it was recently updated,
            # move it to the MRU position.
            self.remove(node)
            self.add(node)

            return

        # Case 2: Key does not exist

        # Create a new node
        node = Node(key, value)

        # Store the node in HashMap
        self.cache[key] = node

        # New node is the Most Recently Used node
        self.add(node)

        # If capacity is exceeded,
        # remove the Least Recently Used node.
        if len(self.cache) > self.capacity:

            # LRU node is immediately before TAIL
            lru = self.tail.prev

            # Remove it from the linked list
            self.remove(lru)

            # Remove it from HashMap
            del self.cache[lru.key]


if __name__ == "__main__":

    capacity = 4

    obj = LRUCache(capacity)

    obj.put(2, 6)
    obj.put(4, 7)
    obj.put(8, 11)
    obj.put(7, 10)

    print(obj.get(2))
    print(obj.get(8))

    obj.put(5, 6)

    print(obj.get(7))

    obj.put(5, 7)

    print(obj.get(5))