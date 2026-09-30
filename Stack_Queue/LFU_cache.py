class Node:

    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value

        # Frequency of this node
        self.freq = 1

        self.prev = None
        self.next = None


class DoublyLinkedList:

    def __init__(self):

        # Dummy head and tail nodes
        #
        # Structure:
        #
        # HEAD <-> Node <-> Node <-> TAIL
        #
        # Head side = Most Recently Used
        # Tail side = Least Recently Used

        self.head = Node()
        self.tail = Node()

        self.head.next = self.tail
        self.tail.prev = self.head

        # Number of actual nodes in this list
        self.size = 0

    def add(self, node):

        # Add node immediately after HEAD.
        #
        # Therefore, this node becomes the
        # Most Recently Used node among nodes
        # having the same frequency.

        node.next = self.head.next
        self.head.next.prev = node

        self.head.next = node
        node.prev = self.head

        self.size += 1

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

        self.size -= 1

    def remove_last(self):

        # The node immediately before TAIL
        # is the Least Recently Used node
        # within this frequency list.

        if self.size == 0:
            return None

        node = self.tail.prev

        self.remove(node)

        return node


class LFUCache:

    def __init__(self, capacity: int):

        self.capacity = capacity

        # Current number of nodes in cache
        self.size = 0

        # HashMap:
        #
        # key -> corresponding Node
        #
        # This gives O(1) access to a key.

        self.cache = {}

        # HashMap:
        #
        # frequency -> DoublyLinkedList
        #
        # Every frequency has its own linked list.
        #
        # Example:
        #
        # freq 1 -> [Node 5, Node 2]
        # freq 2 -> [Node 7, Node 8]
        #
        self.freq_map = {}

        # Minimum frequency currently present
        self.min_freq = 0

    def add_to_frequency_list(self, node):

        # If a linked list for this frequency
        # does not exist, create one.

        if node.freq not in self.freq_map:
            self.freq_map[node.freq] = DoublyLinkedList()

        # Add node at the MRU position
        # of this frequency list.

        self.freq_map[node.freq].add(node)

    def update_frequency(self, node):

        # Store old frequency
        old_freq = node.freq

        # Remove node from its old frequency list
        self.freq_map[old_freq].remove(node)

        # If this was the minimum frequency
        # and no nodes are left at this frequency,
        # increase min_freq.

        if old_freq == self.min_freq:
            if self.freq_map[old_freq].size == 0:
                self.min_freq += 1

        # Increase frequency of the node
        node.freq += 1

        # Add node to the new frequency list
        self.add_to_frequency_list(node)

    def get(self, key: int):

        # Key does not exist
        if key not in self.cache:
            return -1

        # Get node from HashMap
        node = self.cache[key]

        # Accessing a node increases its frequency
        self.update_frequency(node)

        return node.value

    def put(self, key: int, value: int):

        # If capacity is zero,
        # nothing can be stored.

        if self.capacity == 0:
            return

        # Case 1:
        # Key already exists

        if key in self.cache:

            # Get existing node
            node = self.cache[key]

            # Update its value
            node.value = value

            # Since this key was used/updated,
            # increase its frequency.

            self.update_frequency(node)

            return

        # Case 2:
        # Key does not exist

        # If cache is already full,
        # we need to remove the LFU node.

        if self.size == self.capacity:

            # Get the linked list containing
            # the least frequently used nodes.

            lfu_list = self.freq_map[self.min_freq]

            # Among nodes having the same frequency,
            # remove the LRU node.

            lfu_node = lfu_list.remove_last()

            # Remove from HashMap

            del self.cache[lfu_node.key]

            self.size -= 1

        # Create a new node

        node = Node(key, value)

        # New node starts with frequency 1

        self.cache[key] = node

        # Add it to frequency 1 list

        self.add_to_frequency_list(node)

        # Since a new node with frequency 1
        # has been inserted,
        # minimum frequency becomes 1.

        self.min_freq = 1

        self.size += 1


if __name__ == "__main__":

    capacity = 2

    obj = LFUCache(capacity)

    obj.put(1, 10)
    obj.put(2, 20)

    print(obj.get(1))

    obj.put(3, 30)

    print(obj.get(2))
    print(obj.get(3))

    obj.put(4, 40)

    print(obj.get(1))
    print(obj.get(3))
    print(obj.get(4))