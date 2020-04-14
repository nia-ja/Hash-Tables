# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''
    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity


    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)


    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass


    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity


    def insert(self, key, value):
        '''
        Store the value with the given key.

        # Part 1: Hash collisions should be handled with an error warning. (Think about and
        # investigate the impact this will have on the tests)

        # Part 2: Change this so that hash collisions are handled with Linked List Chaining.

        Fill this in.
        '''
        # take the key and value, and put it somewhere in the array
        # get an index for the key
        index = self._hash_mod(key)
        node = self.storage[index]
        # if self.storage[index] is not None:
        #     print("WARN: Collision detected for key " + key)

        # self.storage[index] = LinkedPair(key, value)

        # if no node is found create a new node
        # or if key is the same, overwrite current node with new node
        if node is None or node.key == key:
            self.storage[index] = LinkedPair(key, value)
        # if node is taken -> go and check the next element in LinkedPair -> repeat till node.next is empty -> create new node 
        else:
            while True:
                if node.next is None or node.key == key:
                    node.next = LinkedPair(key, value)
                    break
                node = node.next

    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        # index = self._hash_mod(key)
        # self.storage[index] = None

        index = self._hash_mod(key)
        node = self.storage[index]
        prev = None
        while node.next is not None and node.key != key:
            prev = node
            node = node.next
        if prev is None:
            self.storage[index] = node.next
        else:
            prev.next = node.next


    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        # index = self._hash_mod(key)
        # if self.storage[index] is None:
        #     return None
        # return self.storage[index].value

        index = self._hash_mod(key)
        node = self.storage[index]
        if node == None: 
            return None
        while True:
            if node.key == key:
                return node.value
            node = node.next


    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        # increase number of buckets in the hash table
        self.capacity *= 2
        # copy old values
        old_storage = self.storage
        # create a new array size * 2
        self.storage = [None] * self.capacity
        # copy old values into new storage
        for pair in old_storage:
            node = pair
            while node is not None:
                self.insert(node.key, node.value)
                node = node.next


if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")