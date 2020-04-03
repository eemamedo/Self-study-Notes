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
        node = Node()
        if self.head: #check if llist is empty. If not, then usual deal
            node.setData(data)   
            node.setNext(self.head)
            self.head = node
        else: #if yes, then new data and pointer of head
            node.setData(data)
            self.head = node
            
    def print_list(self):
        curr_val=self.head
        while (curr_val):
            print (curr_val.getData())
            curr_val = curr_val.next
            
    
sll = SinglyLinkedList()
sll.insert_at_front(1)
sll.insert_at_front(2)
sll.insert_at_front(3)
sll.print_list()       
        
        
        
        
        
        
        
        
        
        