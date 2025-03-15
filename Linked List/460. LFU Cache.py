class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.freq = 1
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = Node(None, None)
        self.tail = Node(None, None)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def append(self, node: Node):
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev.next = node
        self.tail.prev = node
        self.size += 1

    def pop(self, node: Node = None) -> Node:
        if self.size == 0:
            return None
        if not node:
            node = self.head.next
        node.prev.next = node.next
        node.next.prev = node.prev
        self.size -= 1
        return node


class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.key_to_node = {}
        self.freq_to_nodes = defaultdict(DoublyLinkedList)
        self.min_freq = 0

    def get(self, key: int) -> int:
        if key not in self.key_to_node:
            return -1
        node = self.key_to_node[key]
        self._update(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return
        if key in self.key_to_node:
            node = self.key_to_node[key]
            node.value = value
            self._update(node)
        else:
            if len(self.key_to_node) >= self.capacity:
                lfu_list = self.freq_to_nodes[self.min_freq]
                node_to_remove = lfu_list.pop()
                del self.key_to_node[node_to_remove.key]
            new_node = Node(key, value)
            self.key_to_node[key] = new_node
            self.freq_to_nodes[1].append(new_node)
            self.min_freq = 1

    def _update(self, node: Node):
        freq = node.freq
        self.freq_to_nodes[freq].pop(node)
        if freq == self.min_freq and self.freq_to_nodes[freq].size == 0:
            self.min_freq += 1
        node.freq += 1
        self.freq_to_nodes[node.freq].append(node)