"""
Linked lists uses nodes to store data.
. Nodes are self referential objects.
. For a singly-linked list, a node points to only the next item in the list.
"""

class Node:
    """
    A Node class that Models the data and next node in a linked list
    """
    data = None;
    next_node = None;

    def __init__(self, data):
        self.data = data;

    def __repr__(self):
        return "<Node data: %s>" % self.data


class LinkedList:
    """
    A linked list class. A linked list only keeps reference to its hed node
    """
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None

    def size(self):
        current = self.head;
        count = 0
        while current:
            count += 1;
            current = current.next_node
        return count

    def add(self, data):
        '''
        O(1) operation
        '''
        new_node = Node(data);
        new_node.next_node = self.head
        self.head = new_node

    def search(self, key):
        """
        since we traverse the list until we find the required element, this operation is a linear runtime operation
        :param key:
        :return:
        """
        current = self.head

        while current:
            if current.data == key:
                return current
            else:
                current = current.next_node
        return None

    def insert(self, data, index):
        """
        inserting a value is a constant time operation but traversing through the list to locate the index to insert
        the new data is a linear runtime operation therefore taking an overall time of O(n)
        """
        if index == 0:
            self.add(data)
        elif index > 1:
            new_node = Node(data)
            position = index
            current_node = self.head
            while position > 1:
                current_node = current_node.next_node
                position -= 1

            prev_node = current_node
            next_node = prev_node.next_node
            prev_node.next_node = new_node
            new_node.next_node = next_node


    def removeAtIndex(self, index):
        """
        for an index of 0, set change the head of the list to the next value.
        upon arriving at key, set that node's value to the next node
        """
        if index == 0:
            self.head = self.head.next_node
        elif index > 0:
            current_node = self.head
            position = index
            while current_node and position > 1:
                position -= 1
                current_node = current_node.next_node
            if current_node:
                prev_node = current_node
                prev_node.next_node = current_node.next_node.next_node

    def removeByKey(self, key):
        '''
        to remove a node by key, we need to know the previous node to point that previous node to the next of the node to be removed.
        . traverse the list. upon finding key-node, set its previous_node's next to the next_node of the current_node
        . if the current data is not the key, set the previous to the current node and the current to the next of the current, ie the now previous node

        '''
        found = False
        prev_node = None
        current_node = self.head
        while current_node and not found:
            if current_node.data == key and current_node is self.head:
                found = True
                self.head = current_node.next_node
            elif current_node.data == key:
                found = True
                prev_node.next_node = current_node.next_node
            else:
                prev_node = current_node
                current_node = current_node.next_node


    def __repr__(self):
        '''
        this operation traverses through the list and creates a string of each nodes data
        Takes O(n) time
        :return: a string representation of the list
        '''
        nodes = []
        current = self.head

        while current:
            if current is self.head:
                nodes.append("[Head: %s]" %self.head)
            elif not current.next_node:
                nodes.append("[Tail: %s]" %current)
            else:
                nodes.append("[%s]" %current)
            current = current.next_node
        return "-> ".join(nodes)

L = LinkedList()
L.add(19)
L.add(20)
L.add(90)
L.removeByKey(90)
print(L )