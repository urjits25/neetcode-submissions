class Node:
    def __init__(self, key = -1, val = -1, prev = None, next = None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev

# remove from tail, add to head

class LRUCache:

    def __init__(self, capacity: int):
        self.head = self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.cap = capacity
        self.key_to_dll = {}

    def get(self, key: int) -> int:
        if key in self.key_to_dll:
            val = self.key_to_dll[key].val
            self.remove(self.key_to_dll[key] )
            self.add(key, val)
            return val
        return -1

    def put(self, key: int, value: int) -> None:
        if key not in self.key_to_dll:
            self.add(key, value)
            if len(self.key_to_dll) > self.cap:
                self.remove(self.tail.prev )
        else:
            self.remove(self.key_to_dll[key] )
            self.add(key, value )
            
    def add(self, key, val):
        # add to dll
        new = Node(key, val, self.head, self.head.next)
        self.head.next.prev = new
        self.head.next = new
        

        # add to hm
        self.key_to_dll[key] = new

    def remove(self, cur):
        # remove from hm
        del self.key_to_dll[cur.key]
        # remove from dll
        cur.prev.next, cur.next.prev = cur.next, cur.prev

        