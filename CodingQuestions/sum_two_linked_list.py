"""
Given an two integers as linked list
sum them and output as a linked list
Input: 
    First List: 5->6->3    (represented number 563)
   Second List: 8->4->2    (represented number 842)
   
Output:
   Result List: 1->4->0->5 (represented number 1405)
"""
class LinkedList:
    class Node:
        def __init__(self, data=None):
            self.data = data
            self.next = None

    def __init__(self):
        self.head = None
        self.size = 0

    def size(self):
        return self.size

    def insert(self, data):
        if self.size == 0:
            self.head = self.Node(data)
            self.size += 1
            return
        new_node = self.Node(data)
        new_node.next = self.head
        self.head = new_node
        self.size += 1

    def to_string(self):
        temp = self.head
        while temp is not None:
            if temp.next is None:
                print str(temp.data)
            else:
                print str(temp.data) + " ->",
            temp = temp.next


def add_two_lst(lst1, lst2):
    stk1 = []
    stk2 = []
    temp_node_lst1 = lst1.head
    temp_node_lst2 = lst2.head
    result = LinkedList()
    carry = 0
    # stores lst1, lst2 into stk1, stk2 respectively
    while True:
        if temp_node_lst1 is not None:
            stk1.append(temp_node_lst1.data)
            temp_node_lst1 = temp_node_lst1.next
        if temp_node_lst2 is not None:
            stk2.append(temp_node_lst2.data)
            temp_node_lst2 = temp_node_lst2.next
        else:
            break
    # pops stk1 and stk2 for addition
    while (len(stk1) > 0) and (len(stk2) > 0):
        sum = stk1.pop() + stk2.pop() + carry
        if sum > 9:
            carry = sum / 10
            result.insert(sum - 10)
        else:
            carry = 0
            result.insert(sum)

    if (len(stk1) > 0):
        temp_stk = stk1
    else:
        temp_stk = stk2
    # if stk1 or stk2 has any data left put into result while adding carry if needed
    while len(temp_stk) > 0:
        sum = temp_stk.pop() + carry
        carry = sum / 10
        if carry > 0:
            result.insert(sum - 10)
        else:
            result.insert(sum)
    if carry > 0:
        result.insert(carry)

    return result


linklst1 = LinkedList()
linklst1.insert(3)
linklst1.insert(6)
linklst1.insert(5)
linklst1.insert(1)
linklst2 = LinkedList()
linklst2.insert(2)
linklst2.insert(4)
linklst2.insert(8)
result = add_two_lst(linklst1, linklst2)
print 'Input:'
print '\tFirst List: ',
linklst1.to_string()
print '\tSecond List: ',
linklst2.to_string()
print 'Output\n\t',
result.to_string()
