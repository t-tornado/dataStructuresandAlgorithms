"""
implementing a linkeed list in Python and calculating the space and time complexity of each operation (add, updating, removing by index and value, calculating size)
"""
class Node:
    '''
    each element in a Singly-linked list is a node that has the reference to the next element
    '''
    data = None
    next_node = None
    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return "<Node data: %s>" % self.data

class Linkedlist:
    '''
    a Linked list only keeps reference to the head of the list only
    '''
    def __init__(self):
        self.head = None

    def size(self):
        current_node = self.head
        count = 0
        while current_node:
            count += 1
            current_node = current_node.next_node
        return count

    def add(self, data):
        '''
        when an item is added to the list, that item becomes the head of the list. and the remaining items are shifted to the right.
        addind an item to the list takes a constant time O(1)
        '''
        new_item = Node(data)
        new_item.next_node = self.head
        self.head = new_item

    def insert(self, data, index):
        '''
        To insert to a specific index in the list, we need to first traverse the list, while keeping count and arrive at a position
        immediately before the required position. This gives us the reference to the previous of the new_node. we can then set the
        next of the new-node to the next of the prev-node and set the next of the prev-node to the new-node
        :param key:
        :return: the item that was inserted.
        '''
        current = self.head
        position = index
        new_node = Node(data)
        if index == 0:
            self.add(data)
        elif index > 0:
            while position > 1 and current :
                position -= 1
                current = current.next_node
            if current:
                prev_node = current
                current = new_node
                current.next_node = prev_node.next_node
                prev_node.next_node = current
            else:
                print('Index out of range')

    def removeAtIndex(self, index):
        '''
        traverse through the list from the head.
        record the current position; ie index as traversing the list
        arrive at the index before the given index.
        if index is 0, set the head to the next of the current head.
        if the index is > 0, set that node as prev-node and set its next-node to the next of its current next-node

        TC = O(n)
        '''
        if index == 0:
            self.head = self.head.next_node
        elif index > 0:
            position = index
            current_node = self.head
            while current_node and position > 1:
                position -= 1
                current_node = current_node.next_node

            prev_node = current_node
            prev_node.next_node = current_node.next_node.next_node

    def removeByKey(self, key):
        '''
        To return none when the key is not found, keep a variable that checks whether the key has been found or not
        traverse the list keeping
        '''


    def __repr__(self):
        '''
       create an array that will store the node values.
       traverse through the list from the head to tail.
       If node is the head, add a head label.
       if node is the tail, add the tail label
       if a node is neither head nor tail, record its data
       after the loop runs through, join the strings in the array into a single string separated with an arrow
        :return: a string representation of the list
        '''
        node_values = []
        current_node = self.head
        while current_node:
            if current_node is self.head:
                node_values.append("<Head: %s>" %self.head.data)
            elif current_node.next_node is None:
                node_values.append("<Tail: %s>" %current_node.data)
            else:
                node_values.append("<Node: %s>" %current_node.data)
            current_node = current_node.next_node

        return '-> '.join(node_values)


        



l = Linkedlist()
l.add(20)
l.add(39)
l.add(34)
print(l)
l.removeAtIndex(2)
print(l)
