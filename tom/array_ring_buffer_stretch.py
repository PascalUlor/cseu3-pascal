class ArrayRingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = 0
        self.storage = [None] * capacity # example : capacity = 4 => [None, None, None, None]

    def append(self, item):
        # set the storage at index of current to item
        self.storage[self.current] = item
        # increment the current ref
        self.current += 1

        # if we reach capacity
        if self.current == self.capacity:
            # set the current ref back to the beginning
            self.current = 0

    def get(self):
        # list comprehension alternative
        # return [item for item in self.storage if item is not None]

        # create list contents = empty list
        list_contents = []
        # iterate over the storage
        for item in self.storage:
            # if the item is not None
            if item is not None:
                # append to the list
                list_contents.append(item)
        
        # return the list contents
        return list_contents