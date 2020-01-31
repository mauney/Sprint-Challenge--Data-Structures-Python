from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        # if length < capacity, add item and assign to current
        if self.storage.length < self.capacity:
            # create node at tail
            self.storage.add_to_tail(item)
            # set head.prev to tail and tail.next to head
            self.storage.head.prev = self.storage.tail
            self.storage.tail.next = self.storage.head
            # set current to head
            self.current = self.storage.head
        # elif length >= capacity,
        else:
            # new value to current; move current
            self.current.value = item
            self.current = self.current.next
        

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # Your code here
        pointer = self.storage.head
        while True:
            if pointer.value is not None:
                list_buffer_contents.append(pointer.value)

            if pointer is self.storage.tail:
                break
            
            pointer = pointer.next

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass


# buffer = RingBuffer(5)
# buffer.append('a')