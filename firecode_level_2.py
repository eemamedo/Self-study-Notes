'''
Write a function that takes in an input string and returns True if all the characters in the string are unique, False if there is even a single repeated character.

Examples:
 
input_string("abcde") -> True

unique_chars_in_string("aa") -> False


def unique_chars_in_string(input_string):
    return sorted(set(input_string)) == sorted(input_string)

input_string = 'aa'
print(unique_chars_in_string (input_string))
'''

'''
Given an list of integers, write a method - max_gain - 
that returns the maximum gain. Maximum Gain is defined as 
the maximum difference between 2 elements in a list such that the larger 
element appears after the smaller element. If no gain is possible, return 0.

Example:
max_gain([100,40,20,10]) ==> 0
max_gain([0,50,10,100,30]) ==> 100
[0,50,10,100,30] => 100

def max_gain(input_list):
    if max(input_list) == input_list[0]:
        return 0
    else:
        return max(input_list) - min(input_list)

input_list = [0,50,10,100,30]
print (max_gain(input_list))
'''

'''
Write a function to insert a node at the front of a Singly Linked-List

LinkedList: 1->2 , Head = 1

insert_at_front(1) ==> 1->1->2

insert_at_front(2) ==> 2->1->2

insert_at_front(3) ==> 3->1->2

Insert at the front end

'''

class Node:
    def __init__(self):
        self.data = None
        self.next = None
     
    def setData(self,data):
        self.data = data
      
    def getData(self):
        return self.data
     
    def setNext(self,next):
        self.next = next
        
    def getNext(self):
        return self.next



class SinglyLinkedList:
    #constructor
    def __init__(self):
        self.head = None
        
    #method for setting the head of the Linked List
    def setHead(self,head):
        self.head = head
                      

    #Create a node object with 7 as the data and the next node pointing 
    #to head node; Point the head pointer to this new node
    
    def insert_at_front(self,data):
        node = Node() #initialize the class
        if self.head: #check if llist is empty. If not, then usual deal
            node.setData(data) #gets new data
            node.setNext(self.head) #step 1: next node of a new data points to current head
            self.head = node # step 2: head now points to the newest node
            print ('this is head', self.head.data) #returns the memory allocation
        else: #if yes, then new data and pointer of head
            node.setData(data)
            self.head = node #Instance of the Node() class. same as self.head = Node(data). To get data in this case: self.head.data
    # If init in Node would have data as passable argument, then self.head = Node(data). But in our case
    # it's not like that; and when we run node.setData(data) it's the same as node=Node(data). 
    # Doing just self.head = node creates an instance of Node (). 
        
    def insertAtEnd(self,data):
        node = Node()
        node.setData(data)
        if self.head is None: #The linked list is empty. Set the head to the current Node and next to None
            self.head = node
    
        else: #It's not empty. In that case you will need to get until the end, and then insert the data
            curr_val = self.head #curr_val is an instance of the class
            while (curr_val.next): #gets the next part of the node (head|next -> data|next)
                curr_val = curr_val.next #traversing until the end   
            curr_val.next = node
            
               
    def print_list(self):
        curr_val=self.head
        while (curr_val):
            print (curr_val.getData())
            curr_val = curr_val.next
            
'''
Mistake I was making was while (curr_val). That is equivalent to curr_val = Node (data). It's not an integer;
rather it's an instance of a class. The reason why it works in print_list is due to print (curr_val.getData()).
If you print curr_val, this is what you get: curr val <__main__.Node object at 0x10ec43310>. Similar thing you 
get with curr_val.next (that one will be pointing to None @ certain point, and terminate the loop).

So, when I was doing while(curr_val) and then doing curr_val.next = node, it is already None. Instead, getNext()
will return the actual integer (curr_val.next). Once it says None, you terminate the loop, and assign it to the actual value.
If you do curr_val.getNext() after curr_val.next (after the loop is terminated), you should get a number. But doing it twice, should get you
None (it does)


      
sll = SinglyLinkedList()
sll.insert_at_front(1)
sll.insert_at_front(2)
sll.insert_at_front(3)
sll.insertAtEnd(7)
sll.print_list()     
'''


'''
class Nodes:
    def __init__(self, data):
        self.data = data
        self.next = None
     
temp = Nodes(10)
node = Nodes(10)
'''      

'''
Given a sorted list of integer ranges (see Range in Use Me), merge all overlapping ranges.
Note: Check out the Use Me section to get the structure of the Range class.


Input List: [[1,10], [5,8], [8,15]] XXXX
[[1,15]]
Input List: [[1,2], [2,5], [8,10], [15,20]] XXXX
[[1,5], [8,10], [15,20]]
Input List: [[1,5], [5,10], [11,15] ,[15,20]] XXXX
[[1,10], [11,20]]
Input List: [[1,4], [3,7], [5,10], [11,15]]
[[1,10], [11,15]]
Input List: [[5,50], [25,100], [150,200]]
[[5,100], [150,200]]
'''      

class Range(object):
    def __init__(self):
        self.lower_bound = -1
        self.upper_bound = -1
    
    def __init__(self,lower_bound,upper_bound):
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound
 
    def __str__(self):
        return "["+str(self.lower_bound)+","+str(self.upper_bound)+"]"

def merge_ranges(input_range_list):
    previous = input_range_list[0]
    output = []
    i=1
    while (i < len(input_range_list)): 
        lb_prev = min(previous)
        ub_prev = max(previous)
        print (lb_prev, ub_prev)
        lb_curr = min (input_range_list[i])
        ub_curr = max (input_range_list[i])
        if (lb_curr <= ub_prev):
            merged = [lb_prev, max(ub_prev,ub_curr)]
            previous = merged
            print ('prev', previous)
        else:
            output.append(previous)
            current = [lb_curr,ub_curr]
            previous = current
            print ('prev2', current)
        i=i+1
    output.append(previous)
    return output



input_range_list = [[1,2], [2,5], [8,10], [15,20]]
output =  merge_ranges(input_range_list)
arr = [1,2]




        
        
        
        