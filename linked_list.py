class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add_nodes(self, *args):
        child_head, child_tail = None, None
        for data in args:
            new_node = Node(data)
            if not child_head:
                child_head = child_tail = new_node
            else:
                child_tail.next = new_node
                child_tail = new_node
                
        if not self.head:
            self.head = child_head
            return

        tail = self.head
        while tail.next:
            tail = tail.next
        tail.next = child_head

    def remove_from_end(self):
        if not self.head:
            return None  # Or raise an exception

        if not self.head.next:
            data = self.head.data
            self.head = None
            return data

        current = self.head
        while current.next.next:
            current = current.next
        data = current.next.data
        current.next = None
        return data

    def remove_node(self, node):
        if not self.head:
            return False # Or raise exception

        if self.head == node:
            self.head = self.head.next
            return True

        current = self.head
        while current.next:
            if current.next == node:
                current.next = current.next.next
                return True
            current = current.next
        return False

    def print_all(self):
        elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            current = current.next
        print(" -> ".join(elements))


if __name__ == '__main__':
    linked_list = LinkedList()
    linked_list.add_nodes(1, 2, 3)
    linked_list.print_all()  # Expected: 1 -> 2 -> 3

    linked_list.remove_from_end()
    linked_list.print_all()  # Expected: 1 -> 2

    node_to_remove = linked_list.head.next  # Node with data 2
    linked_list.remove_node(node_to_remove)
    linked_list.print_all()  # Expected: 1

    linked_list.remove_node(linked_list.head)
    linked_list.print_all() # Expected:

    linked_list.add_nodes(4)
    linked_list.add_nodes(5)
    linked_list.add_nodes(6)

    node_to_remove = linked_list.head.next.next # Node with data 6
    linked_list.remove_node(node_to_remove)
    linked_list.print_all() # Expected 4 -> 5

    linked_list.add_nodes(7, 8, 9)
    linked_list.print_all()  # Expected 4 -> 5 -> 7 -> 8 -> 9