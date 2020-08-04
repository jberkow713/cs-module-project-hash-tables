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
        
        
        node = self.hashTable[index]
        
        # so if is value at specific index is empty, 
        # use HashTableEntry Class to input value specified by key, 
        
        
        
        # if the specific index is empty
        #insert actual HashTableEntry class instance with a key and value
        if node is None:
        
            self.hashTable[index] = HashTableEntry(key, value)
		    
            return  

        # if the specific index is not empty, set a variable = to the index called 
        # whatever the hell you want, in this case, current
        # current means absolutely nothing, besides a reference point to the specific
        # index which your value has returned, and in this case, = to node as well
        
        # so i THINK that this outside node is set to whenever the "current" inside
        # of the loop is set to, which is why it has to be set outside as well
        # when current inside of the loop is set to the next node's position,
        # the current outside of the loop is also set to that node, so that when you 
        # exit the while loop, and hit the None value,
        # you can actually use current's position to insert the following Node
        current = node
	    
        while node is not None:
            #this just allows you to replace old value with new value, if key is same    
            if node.key == key:
                self.hashTable[index] = HashTableEntry(key, value)

            
            
            current = node

            #this is like saying the index = the next index 
            node = node.next
		    #so this is how a while loop works: Current is a variable representing 
            #the index position. While the index position is filled, node
            # aka the index position, moves to the next index position,
            # and if that position is once again filled,  you move to the beginning of the
            # while loop, and set "current"'s index position
            # again equal to that new variable, node, it scrolls along as node scrolls along
            # but always one index position behind node

            # the index position then scrolls along the linked list, 
            # until it finds a NONE value
            # you are then kicked out of the WHILE LOOP, and of course you have to set 
            #current.next's position to the node.next's position, 
            # because when you exit the while loop,
            # you do so from the bottom, which means current hasn't 
            # been updated into node's next index yet
            
            # so you exit the while loop, 
            # set current.next equal to the nodes index value which
            # equaled None, and then you simply insert the HashTableEntry, or 
            # node class with key and value, as before
            
	
    # Basically, the node is the scroller through the linked list, and current
    # is the object
        current.next = HashTableEntry(key, value)
        

        
        
      

        
    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        index = self.hash_index(key)
        node = self.hashTable[index]
        #if the key's value equals specified value,
        # make the value at that index = None,
        # return the value
        if node.key == key:
            
            node.value = None
            value = node.value
            return value
        
        current = node
	    
        while node.key != key:
                       
            current = node
            
            node = node.next

            if node.key is None:
                return None
            else:
                result = node.value
                current.next = current.next.next 
                return result 

                #set the previous's next value = node.next's value
                # and return the value of Node,
                # this will sever the connection to the Node, and basically delete it

                
        
        
        
        #if node is None:
        #    print("Warning, not found")
        #    return node 
        
        #else:

            
        #    node.value = None

        #so if you scroll to the index position where the value is supposed to be
        # but you don't see the value, becasue another value is in it's spot,
        # you have to scroll along the linked list until you get to the specific value 
        # represented by the key, and THEN delete the node by basically making 
        # the connection to the Node non existent    

        


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
        #head to the index value specified by the key:
        # if the node is filled but the key is not the specified key,
        # scroll alone the linked list from the starting index, one by one
        #if you reach none and have not yet found the key, just return None, 
        # meaning you did not find the value for this specific key
        # otherwise, if you find the key within this linked list, return the value
        #while node is not None and node.key != key:
        if node.key == key:
            return node.value 
        
        while  node.key != key:

            node = node.next 

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
