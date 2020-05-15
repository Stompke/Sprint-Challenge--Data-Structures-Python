class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def reverse_list(self, node, prev):
        # Is the list empty?
        if self.head:
            # Does the list contain more than 1 node?
            if self.head.get_next():
                # Is it the first node?
                if node is self.head:
                    self.reverse_list(node.next_node, node)
                # Is it a middle node?
                elif node.get_next():
                    self.add_to_head(node.value)
                    self.reverse_list(node.next_node, node)
                    prev.set_next(None)
                # Is it the last node?
                elif node.get_next() is None:
                    self.add_to_head(node.value)
                    prev.set_next(None)

        


ll = LinkedList()
ll.add_to_head(1)
ll.add_to_head(2)
ll.add_to_head(3)
# ll.add_to_head(4)
# ll.add_to_head(5)
# print(ll.head.value)
# print(ll.head.next_node.value)
# print(ll.head.next_node.next_node.value)
# 
# print("Get Head 1: ", ll.head.get_value())
print(ll.head.value)
print(ll.head.next_node.value)
print(ll.head.next_node.next_node.value)
print('Reverse List: ', ll.reverse_list(ll.head, None))
# print("Get Head 2: ", ll.head.get_value())
print(ll.head.value)
print(ll.head.next_node.value)
print(ll.head.next_node.next_node.value)
# print(ll.head.next_node.next_node.next_node.value)
# print(ll.head.next_node.next_node.next_node.next_node.value)
# print(ll.head.next_node.next_node.next_nodevalue)