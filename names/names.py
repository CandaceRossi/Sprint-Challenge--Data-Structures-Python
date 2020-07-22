from sys import maxsize
import time


class Queue:
    def __init__(self, value):
        self.size = 0
    #add the first node to the queue
        self.storage = LinkedList()

    def __len__(self):
        return self.size

    def enqueue(self, value):
       #add the new value to the tail of our list
        self.size += 1
        self.storage.add_to_tail(value)

    def dequeue(self):
        if self.size == 0:
            return None
        #remove the value from the head of our list
        self.size -= 1
        value = self.storage.remove_head()
        return value


class Stack:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def __len__(self):
        return self.size

    def push(self, value):
        self.size += 1
    # add an element to front of our array
        self.storage.add_to_tail(value)

    def pop(self):
        if self.size == 0:
            return None
        self.size -= 1
        node = self.storage.remove_tail()
        return node


class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

class LinkedList:
    def __init__(self):
        self.head = None  # Stores a node, that corresponds to our first node in the list
        self.tail = None  # stores a node that is the end of the list

    def __str__(self):  # return all values in the list a -> b -> c -> none
        output = ''
        current_node = self.head  # create a tracker node variable
        while current_node is not None:  # loop until its None
            output += f'{current_node.value} ->'
            # update the tracker node to the next node
            current_node = current_node.next_node
        return output

    def add_to_head(self, value):
        # create a node to add
        new_node = Node(value)
    # check if list is empty
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
          # new_node should point to current head
            new_node.next_node = self.head
      # move head to new node
            self.head = new_node

    def add_to_tail(self, value):
        # create a node to add
        new_node = Node(value)
    # check if list is empty
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
          # point the node at the current tail, to the new node
            self.tail.next_node = new_node
            self.tail = new_node

  # remove the head and return its value
    def remove_head(self):
        # if list is empty, do nothing
        if not self.head:
            return None
    # if list only has one element, set head and tail to None
        if self.head.next_node is None:
            head_value = self.head.value
            self.head = None
            self.tail = None
            return head_value
    # otherwise we have more elements in the list
        head_value = self.head.value
        self.head = self.head.next_node
        return head_value

    def contains(self, value):
        if self.head is None:
            return False

    # Loop through each node, until we see the value, or we cannot go further
        current_node = self.head

        while current_node is not None:
          # check if this is the node we are looking for
            if current_node.value == value:
                return True

      # otherwise, go to the next node
            current_node = current_node.next_node
        return False

    def isEmpty(self, value):
        return True if self.head.value is None else False

    def get_max(self, value):
        if (self.isEmpty(self.head.value)):
            return str(-maxsize - 1)

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # take the current value of our node (self.value)
        # compare to the new value we want to insert
    
        if value < self.value:
                # If self.left is already taken by a node
                # make that (left) node, call insert
                # set the left child to the new node with new value
            if self.left is None:
                self.left = BSTNode(value)
            else: 
                self.left.insert(value)

        if value >= self.value: 
               # If self.right is already taken by a node
               # make that (right) node call insert
               # set the right child to the new node with new value
            if self.right is None:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)            

    # Return True if the tree contains the value
    # False if it does not

    def contains(self, target):
        if self.value == target:
            return True
        # compare the target to current value
        # if current value is more than target
        found = False
        if self.value >= target:
            # check the left subtree (self.left.contains(target))
            # if you cannot go left, return False
            if self.left is None:
                return False
            found = self.left.contains(target)

        # if current value >= target
        if self.value < target:
            # check if right subtree contains target
            # if you cannot go right, return false
            if self.right is None:
                return False
            found = self.right.contains(target)
        
        return found


    # Return the maximum value found in the tree
    def get_max(self):
        if self.right is None:
            return self.value
        return self.right.get_max()     

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        #call function on the current value fn(self.value)
        fn(self.value)
       #if you can go left, call for_each on the left tree
        if self.left:
            self.left.for_each(fn) 
       #if you can go right, call for_each on the left tree
        if self.right:
            self.right.for_each(fn)
    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        fn(self.node)
        if self.left:
            return self.left.for_each(fn)
        print(self.node) 


    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        #create a queue for nodes
        # Base Case
        if node is None:
            return
     # Create an empty queue for level order traversal
        queue = []
    # Enqueue Root and initialize height
        queue.push(node)
        #while queue is not empty
        while(len(queue) > 0):
            print(queue[0].value)

            curr = queue.dequeue()
            print(curr.value)
            #remove the first node from the queue
            node = queue.pop(0)
            #print the removed node
            #add all children into the queue
            #Enqueue left child
            if node.left is not None:
                queue.append(node.left)

            # Enqueue right child
            if node.right is not None:
                queue.append(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        # Base Case
        if node is None:
            return
         #create a stack for nodes
        stack = Stack()
        #add the first node to the stack
        stack.append(node)
        #while stack is not empty
        while(len(stack) > 0):
            print(stack[0].value)
            #remove the first node from the stack
            #print the removed node
            #add all children into the stack




start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
for name_1 in names_1:
    for name_2 in names_2:
        if name_1 == name_2:
            duplicates.append(name_1)

tree = BSTNode(names_2[0])
for name in names_2:
    tree.insert(name)

for name1 in name_1:
    if tree.contains(name1):
        duplicates.append(name1)

end_time = time.time()
# print(len(duplicates))
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
