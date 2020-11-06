class Node: 
	
	# Class to create nodes of linked list 
	# constructor initializes node automatically 
	def __init__(self,data): 
		self.data = data 
		self.next = None
	
class Stack: 
    '''Implementing LIFO Stack ADT using LL'''
	
	# head is default NULL 
	def __init__(self): 
		self.head = None
        self.size = 0
	
	# Checks if stack is empty 
	def isempty(self): 
		if self.head == None: 
			return True
		else: 
			return False

    def len(self):
        return self.size
	
	# Method to add data to the stack 
	# adds to the start of the stack 
	def push(self,data): 
		
		if self.head == None: 
			self.head=Node(data) 
        newnode = Node(data) 
        newnode.next = self.head 
        self.head = newnode 
        self.size += 1

	# Remove element that is the current head (start of the stack) 
	def pop(self): 
		
		if self.isempty(): 
			return None
        # Removes the head node and makes 
        #the preceeding one the new head 
        poppednode = self.head 
        self.head = self.head.next
        poppednode.next = None
        self.size -= 1
        return poppednode.data 
	
	# Returns (but doesn't remove) the head node data 
	def peek(self): 
		if self.isempty(): 
			return None
        return self.head.data 
	
	# Prints out the stack	 
	def display(self): 
		iternode = self.head 
		if self.isempty(): 
			print("Stack Underflow") 
   
        while(iternode != None):          
            print(iternode.data,"->",end = " ") 
            iternode = iternode.next
        #return
		
# Driver code 
MyStack = Stack() 

MyStack.push(11) 
MyStack.push(22) 
MyStack.push(33) 
MyStack.push(44) 

# Display stack elements 
MyStack.display() 

# Print top element of stack 
print("\nTop element is ",MyStack.peek()) 

# Delete top elements of stack 
MyStack.pop() 
MyStack.pop() 

# Display stack elements 
MyStack.display() 

# Print top element of stack 
print("\nTop element is ", MyStack.peek()) 


##################################################

class Node:
    def __init__(self, data):
       self.data = data
       self.next = None
 
class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def _len(self):
        return self.size

    def is_empty(self):
        return self.size == 0    

    def enqueue(self, data):
        '''any new item enters at the tail of the queue, so Enqueue adds an item to the tail of a queue.'''
        if self.tail is None:
            self.head = Node(data) 
            self.tail = self.head
        else:
            self.tail.next = Node(data)
            self.tail = self.tail.next
        self.size += 1
 
    def dequeue(self):
        if self.head is None:
            return None
        else:
            to_return = self.head.data
            self.head = self.head.next
            return to_return


#####################################################################################
'''
Double Linked List
References: https://stackabuse.com/doubly-linked-list-with-python-examples/
'''

class Node:
    def __init__(self, data):
        self.item = data
        self.nref = None #reference to the next node
        self.pref = None #reference to the previous node

class DoublyLinkedList:
    def __init__(self):
        self.start_node = None

    def insert_in_emptylist(self, data):
        if self.start_node is None:
            new_node = Node(data)
            self.start_node = new_node
        else:
            print("list is not empty")        

    def insert_at_start(self, data):
        '''
        To insert an item at the beginning of the doubly linked list, we have to first check whether the list is 
        empty or not. If the list is empty, we can simply use the logic defined in the insert_in_emptylist() 
        to insert the element since in an empty list, the first element is always at the start.

        Else, if the list is not empty, we need to perform three operations:
        1. For the new node, the reference to the next node will be set to self.start_node.
        2. For the self.start_node the reference to the previous node will be set to the newly inserted node.
        3. Finally, the self.start_node will become the newly inserted node.
        '''
        if self.start_node is None:
            new_node = Node(data)
            self.start_node = new_node
            print("node inserted")
            return
        new_node = Node(data)
        new_node.nref = self.start_node
        self.start_node.pref = new_node
        self.start_node = new_node

    def insert_at_end(self, data):
        '''
        Inserting an element at the end of the doubly linked list is somewhat similar to inserting an element at the start. 
        At first, we need to check if the list is empty. If the list is empty then we can simply use the 
        insert_in_emptylist() method to insert the element. If the list already contains some element, we traverse through 
        the list until the reference to the next node becomes None. When the next node reference becomes None it means that
        the current node is the last node. The previous reference for the new node is set to the last node, and the next 
        reference for the last node is set to the newly inserted node.
        '''
        if self.start_node is None:
            new_node = Node(data)
            self.start_node = new_node
            return
        n = self.start_node
        while n.nref is not None:
            n = n.nref
        new_node = Node(data)
        n.nref = new_node
        new_node.pref = n

    def insert_after_item(self, x, data):
        '''
        To insert an item after another item, we first check whether or not the list is empty. If the list is actually empty, 
        we simply display the message that the "list is empty".
        Otherwise we iterate through all the nodes in the doubly linked list. In case if the node after which we want to insert 
        the new node is not found, we display the message to the user that the item is not found. Else if the node is found, 
        it is selected and we perform four operations:
        1. Set the previous reference of the newly inserted node to the selected node.
        2. Set the next reference of the newly inserted node to the next reference of the selected.
        3. If the selected node is not the last node, set the previous reference of the next node after the selected node to the newly added node.
        4. Finally, set the next reference of the selected node to the newly inserted node.

        Example: DoublyLinkedList().insert_after_item(50, 65)
        '''
        if self.start_node is None:
            print("List is empty")
            return
        else:
            n = self.start_node
            while n is not None:
                if n.item == x:
                    break
                n = n.nref
            if n is None:
                print("item not in the list")
            else:
                new_node = Node(data)
                new_node.pref = n #based on the while loop, now n is the node that has X we want.
                new_node.nref = n.nref
                if n.nref is not None:
                    n.nref.prev = new_node
                n.nref = new_node

    def insert_before_item(self, x, data):
        '''
        Iterate through all the nodes. If the node is found:
        1. Set the next reference of the newly inserted node to the selected node.
        2. Set the previous reference of the newly inserted node to the previous reference of the selected.
        3. Set the next reference of the node previous to the selected node, to the newly added node.
        4. Finally, set the previous reference of the selected node to the newly inserted node.
        '''

        if self.start_node is None:
            print("List is empty")
            return
        else:
            n = self.start_node
            while n is not None:
                if n.item == x:
                    break
                n = n.nref
            if n is None:
                print("item not in the list")
            else:
                new_node = Node(data)
                new_node.nref = n
                new_node.pref = n.pref
                if n.pref is not None:
                    n.pref.nref = new_node
                n.pref = new_node

    def delete_at_start(self):
        '''
        Set the value of the start node to the next node and then set the previous reference of the start node to None. 
        However before we do that we need to perform two checks. First, we need to see if the list is empty. 
        And then we have to see if the list contains only one element or not. If the list contains only one element
        then we can simply set the start node to None
        '''
        if self.start_node is None:
            print("The list has no element to delete")
            return 
        if self.start_node.nref is None:
            self.start_node = None
            return
        self.start_node = self.start_node.nref #head is assigned to the next node in the LL
        self.start_prev = None

    def delete_at_end(self):
        '''
        If the list has more than one element, we iterate through the list until the last node is reached. 
        Once we reach the last node, we set the next reference of the node previous to the last node, to None which 
        actually removes the last node. 
        '''
        if self.start_node is None:
            print("The list has no element to delete")
            return 
                    
        if self.start_node.nref is None:
            self.start_node = None
            return
        n = self.start_node
        while n.nref is not None:
            n = n.nref
        n.pref.nref = None

    def delete_element_by_value(self, x):
        # Check if the list is Empty
        if self.start_node is None:
            print("The list has no element to delete")
            return 
        # Check if the list has a single element and if yes,
        # is it actually the element we need.  
        if self.start_node.nref is None:
            if self.start_node.item == x:
                self.start_node = None
            else:
                print("Item not found")
            return 
        # Case when the list has more than one items but the 
        # item to be deleted is the first item. 
        # Here, logic is the same as what we have for the 
        # delete_at_start()
        if self.start_node.item == x:
            self.start_node = self.start_node.nref
            self.start_node.pref = None
            return

        # Case when the list is not empty and the item to be 
        # deleted is not the first; we need to traverse the elements
        # and see if any of the nodes has the value that matches
        # the value to be deleted. 
        # If the node is found, then:
        # 1. Set the value of the next reference of the previous node to 
        # the next reference of the node to be deleted.
        # 2. Set the previous value of the next node to the previous reference 
        # of the node to be deleted 
        n = self.start_node
        while n.nref is not None:
            if n.item == x:
                break
            n = n.nref
        if n.nref is not None:
            n.pref.nref = n.nref
            n.nref.pref = n.pref
        else:
            if n.item == x:
                n.pref.nref = None
            else:
                print("Element not found")        


    def reverse_linked_list(self):
        '''
        To reverse the DLL:
        1. The next reference of the start node should be set none because the first node will become the last 
        node in the reversed list.
        2. The previous reference of the last node should be set to None since the last node will become the previous node.
        3. The next references of the nodes (except the first and last node) in the original list should be swapped 
        with the previous references.

        OG implementation:
        if self.start_node is None:
            print("The list has no element to delete")
            return 
        p = self.start_node #p = 1
        q = p.nref # q = 2
        p.nref = None #It will become the last node, and thus, next reference will be None
        p.pref = q #p.pref = 2
        while q is not None:
            q.pref = q.nref #q.pref = 3; 2;
            q.nref = p #q.nref = 1; 2;
            p = q # p = 2; 1;
            q = q.pref # q = 1; None
        self.start_node = p

        '''
        temp = None
        if self.start_node is None:
            print("The list has no element to delete")
            return 
        curr = self.start_node
        while curr:
            temp = curr.pref
            curr.pref = curr.nref
            curr.nref = temp
            curr = curr.pref
        if temp:
            self.start_node = curr.pref



'''
# YouTube Video: https://www.youtube.com/watch?v=SQHvcLvqq_Q    
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        if self.head is None:
            new_node = Node(data)
            new_node.prev = None
            self.head = new_node
        else:
            new_node = Node(data)
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node
            new_node.prev = cur
            new_node.next = None

    def prepend(self, data):
        if self.head is None:
            new_node = Node(data)
            new_node.prev = None 
            self.head = new_node
        else:
            new_node = Node(data)
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
            new_node.prev = None

    def print_list(self):
        cur = self.head
        while cur:
            print(cur.data)
            cur = cur.next

    def add_after_node(self, key, data):
        cur = self.head
        while cur:
            if cur.next is None and cur.data == key:
                self.append(data)
                return 
            elif cur.data == key:
                new_node = Node(data)
                nxt = cur.next
                cur.next = new_node
                new_node.next = nxt
                new_node.prev = cur
                nxt.prev = new_node
            cur = cur.next

    def add_before_node(self, key, data):
        cur = self.head
        while cur:
            if cur.prev is None and cur.data == key:
                self.prepend(data)
                return
            elif cur.data == key:
                new_node = Node(data)
                prev = cur.prev
                prev.next = new_node
                cur.prev = new_node
                new_node.next = cur
                new_node.prev = prev
            cur = cur.next

    def delete(self, key):
        cur = self.head
        while cur:
            if cur.data == key and cur == self.head:
                # Case 1:
                if not cur.next:
                    cur = None 
                    self.head = None
                    return

                # Case 2:
                else:
                    nxt = cur.next
                    cur.next = None 
                    nxt.prev = None
                    cur = None
                    self.head = nxt
                    return 

            elif cur.data == key:
                # Case 3:
                if cur.next:
                    nxt = cur.next 
                    prev = cur.prev
                    prev.next = nxt
                    nxt.prev = prev
                    cur.next = None 
                    cur.prev = None
                    cur = None
                    return

                # Case 4:
                else:
                    prev = cur.prev 
                    prev.next = None 
                    cur.prev = None 
                    cur = None 
                    return 
            cur = cur.next

    def reverse(self):
        tmp = None
        cur = self.head
        while cur:
            tmp = cur.prev
            cur.prev = cur.next
            cur.next = tmp
            cur = cur.prev
        if tmp:
            self.head = tmp.prev


dllist = DoublyLinkedList()
dllist.append(1)
dllist.append(2)
dllist.append(3)
dllist.append(4)

dllist.reverse()
dllist.print_list()
'''

        


    






