"""
Given a binary tree, design an algorithm which creates a linked list
of all the nodes at each depth(e.g., if you have a tree with depth D,
you'll have D linked lists).
"""


class TreeNode:

    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None

    def add_children(self, left_child, right_child):
        self.left_child = left_child
        self.right_child = right_child


class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None
        self.next = None
        self.size = 0

    def is_empty(self):
        if self.size is 0:
            return True

        else:
            return False

    def insert_end(self, data):
        new_node = Node(data)

        if self.is_empty():
            self.head = new_node

        else:
            focus_node = self.head
            while(focus_node.next is not None):
                focus_node = focus_node.next
            focus_node.next = new_node

        self.size += 1

    def to_string(self):
        focus_node = self.head
        while(focus_node.next is not None):
            print focus_node.data, "->",
            focus_node = focus_node.next

        print focus_node.data


class Queue:

    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0

    def is_empty(self):
        if self.size == 0:
            return True

        else:
            return False

    def enqueue(self, data):
        new_node = Node(data)

        if self.is_empty():
            self.first = new_node
            self.last = self.first

        else:
            old_last = self.last
            self.last = new_node
            old_last.next = self.last

        self.size += 1

    def dequeue(self):
        if self.is_empty():
            return "Empty"

        data = self.first.data
        self.first = self.first.next
        self.size -= 1
        return data

    def to_string(self):
        if self.is_empty():
            print "Empty"

        else:
            focus_node = self.first
            while focus_node is not None:
                print focus_node.data,
                focus_node = focus_node.next


def create_tree_node_list(values):
    tree_node_list = []
    for value in values:
        tree_node_list.append(TreeNode(value))

    return tree_node_list


def create_depth_linked_lists(root):
    if root is None:
        return "Empty"

    lsts = []
    queue = Queue()
    queue.enqueue((root, 0))

    while queue.is_empty() is not True:
        current_tple = queue.dequeue()
        if len(lsts) == 0 or len(lsts) <= current_tple[1]:
            lsts.append(LinkedList())

        if current_tple[0].left_child is not None:
            queue.enqueue((current_tple[0].left_child, current_tple[1]+1))

        if current_tple[0].right_child is not None:
            queue.enqueue((current_tple[0].right_child, current_tple[1]+1))

        lsts[current_tple[1]].insert_end(current_tple[0].data)

    return lsts


def print_linked_lists(lsts):
    for lst in lsts:
        lst.to_string()

