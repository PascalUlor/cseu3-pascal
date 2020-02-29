from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        # is the storage full to capacity? if not...
        if self.storage.length < self.capacity:
            # add to the tail of the storage list
            self.storage.add_to_tail(item)
            # set the current to the tail of the storage
            self.current = self.storage.tail
        
        # if the storage hits the capacity...
        if self.storage.length == self.capacity:
            # set the currents value to the item
            self.current.value = item
            # does the current ref point to the tail?...
            if self.current is self.storage.tail:
                # set the current to the head
                self.current = self.storage.head
            # otherwise
            else:
                # set the current to the currents next
                self.current = self.current.next                

    def get(self):
        list_contents = []
        # set the current ref to the storage head
        current = self.storage.head
        # iterate over the list until the current ref points to none
        while current:
            # append the current value to the list contents
            list_contents.append(current.value)
            # increment: set the current ref to the currents next
            current = current.next
        
        # return the list contents
        return list_contents