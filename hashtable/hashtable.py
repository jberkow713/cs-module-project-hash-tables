class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        self.capacity = capacity 
        #this hashtable represents a list of lists, for 
        # i in range of capacity
        self.hashTable = [None] * capacity  

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        # Your code here


    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here


    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # Your code here


    def djb2(self, key):
        hash = 5381
        for c in key:
            hash = (hash * 33) + ord(c)
        return hash


    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        #return self.fnv1(key) % self.capacity
        #basically runs a specific key through the djb2 function, gets an integer value,
        #  then takes module(whatever capacity is) of that integer value, and tells where
        # specific key should be within hash table, by returning specific index 
        
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.

        """
        #so given key should return a hash_index, and then you just want to store the 
        # specific value at that index , so like "Jesse": "Hero", Hero is the value, 
        # Jesse is the key, so let's use the Hash_index to store the value of given key
        
        #index position in table
        # get index from hash_index function, based off djb2 func
        # use that index in hashtable to append specified value
        #by using the HashTableEntry class with a key and value
        
        

        index = self.hash_index(key)
        
        
        #node = self.hashTable[index]
        
        # so if is value at specific index is empty, 
        # use HashTableEntry Class to input value specified by key, 
        self.hashTable[index] =  HashTableEntry(key, value)
        
        #if node is None:
        
        #    self.hashTable[index] = HashTableEntry(key, value)
		    
        #    return  
        #else:

        #    self.hashTable[index] = HashTableEntry(key, value)
		    
        #    return  


        #set new variable equal to the node's value 
        #current = node
	    #if the node you're looking to enter the info on 
        #already has something stored inside of it, 

        #while node is not None:
        #    current = node
		    
        #    node = node.next
	# Add a new node at the end of the list with provided key/value
        #current.next = HashTableEntry(key, value)
        

        
        
      

        
    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        index = self.hash_index(key)
        node = self.hashTable[index]

        if node is None:
            print("Warning, not found")
        else:
            
            node.value = None

        


    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Your code here
        # node represents the object at the point where the index is
        #request value specific to index that key and hash function bring you to
        index = self.hash_index(key)
        node = self.hashTable[index]
        if node is None:
            return None
        else:
            return node.value


    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here



if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
