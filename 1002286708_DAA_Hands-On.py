class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def insert(self, key, value):
        new_node = Node(key, value)
        if not self.head:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
    
    def remove(self, key):
        current = self.head
        while current:
            if current.key == key:
                if current.prev:
                    current.prev.next = current.next
                if current.next:
                    current.next.prev = current.prev
                if current == self.head:
                    self.head = current.next
                if current == self.tail:
                    self.tail = current.prev
                return True
            current = current.next
        return False
    
    def search(self, key):
        current = self.head
        while current:
            if current.key == key:
                return current.value
            current = current.next
        return None
    
    def clear(self):
        self.head = self.tail = None

class HashTable:
    def __init__(self, capacity=8):
        self.capacity = capacity
        self.size = 0
        self.table = [DoublyLinkedList() for _ in range(capacity)]
    
    def _hash(self, key):
        A = 0.6180339887  # Fractional part of the golden ratio
        return int(self.capacity * ((key * A) % 1))
    
    def _resize(self, new_capacity):
        new_table = [DoublyLinkedList() for _ in range(new_capacity)]
        for dll in self.table:
            current = dll.head
            while current:
                new_index = current.key % new_capacity  # Division method for rehashing
                new_table[new_index].insert(current.key, current.value)
                current = current.next
        self.table = new_table
        self.capacity = new_capacity
    
    def insert(self, key, value):
        index = self._hash(key)
        self.table[index].insert(key, value)
        self.size += 1
        if self.size >= self.capacity:
            self._resize(self.capacity * 2)
    
    def remove(self, key):
        index = self._hash(key)
        if self.table[index].remove(key):
            self.size -= 1
            if self.size > 0 and self.size <= self.capacity // 4:
                self._resize(self.capacity // 2)
            return True
        return False
    
    def search(self, key):
        index = self._hash(key)
        return self.table[index].search(key)

# Example usage
if __name__ == "__main__":
    ht = HashTable()
    ht.insert(1, 100)
    ht.insert(2, 200)
    ht.insert(3, 300)
    ht.insert(10, 1000)
    
    print("Value for key 2:", ht.search(2))
    ht.remove(2)
    print("Value for key 2 after deletion:", ht.search(2))
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def insert(self, key, value):
        new_node = Node(key, value)
        if not self.head:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
    
    def remove(self, key):
        current = self.head
        while current:
            if current.key == key:
                if current.prev:
                    current.prev.next = current.next
                if current.next:
                    current.next.prev = current.prev
                if current == self.head:
                    self.head = current.next
                if current == self.tail:
                    self.tail = current.prev
                return True
            current = current.next
        return False
    
    def search(self, key):
        current = self.head
        while current:
            if current.key == key:
                return current.value
            current = current.next
        return None
    
    def clear(self):
        self.head = self.tail = None

class HashTable:
    def __init__(self, capacity=8):
        self.capacity = capacity
        self.size = 0
        self.table = [DoublyLinkedList() for _ in range(capacity)]
    
    def _hash(self, key):
        A = 0.6180339887  # Fractional part of the golden ratio
        return int(self.capacity * ((key * A) % 1))
    
    def _resize(self, new_capacity):
        new_table = [DoublyLinkedList() for _ in range(new_capacity)]
        for dll in self.table:
            current = dll.head
            while current:
                new_index = current.key % new_capacity  # Division method for rehashing
                new_table[new_index].insert(current.key, current.value)
                current = current.next
        self.table = new_table
        self.capacity = new_capacity
    
    def insert(self, key, value):
        index = self._hash(key)
        self.table[index].insert(key, value)
        self.size += 1
        if self.size >= self.capacity:
            self._resize(self.capacity * 2)
    
    def remove(self, key):
        index = self._hash(key)
        if self.table[index].remove(key):
            self.size -= 1
            if self.size > 0 and self.size <= self.capacity // 4:
                self._resize(self.capacity // 2)
            return True
        return False
    
    def search(self, key):
        index = self._hash(key)
        return self.table[index].search(key)

# Example usage
if __name__ == "__main__":
    ht = HashTable()
    ht.insert(1, 100)
    ht.insert(2, 200)
    ht.insert(3, 300)
    ht.insert(10, 1000)
    
    print("Value for key 2:", ht.search(2))
    ht.remove(2)
    print("Value for key 2 after deletion:", ht.search(2))
