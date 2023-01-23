class LinkedList:
  #-------------------------- nested _Node class --------------------------
  class _Node:
    __slots__ = '_element', '_next'         # streamline memory usage
    def __init__(self, element, next):
      self._element = element
      self._next = next
  #------------------------------- list methods -------------------------------
  def __init__(self):
    self._head = None
    self._tail = None
    self._size = 0  

  def __len__(self):
    return self._size

  def is_empty(self):
    return self._size == 0
    
  def front(self):
    if self.is_empty():
      raise ValueError('list is empty')
    return self._head._element              # front aligned with head of list

  def remove_front(self):
    if self.is_empty():
      raise ValueError('list is empty')
    answer = self._head._element
    self._head = self._head._next
    self._size -= 1
    if self.is_empty():                     # special case as list is empty
      self._tail = None                     # removed head had been the tail
    return answer
  
  def add_to_front(self, e):
      self._head = self._Node(e, self._head)   
      if self.is_empty():
            self._tail = self._head
      self._size += 1
  
  def add_to_rear(self, e):
      newest = self._Node(e, None)            # node will be new tail node
      if self.is_empty():
          self._head = newest                   # special case: previously empty
      else:
          self._tail._next = newest
      self._tail = newest                     # update reference to tail node
      self._size += 1

  def __repr__(self):
      elements = []
      cursor = self._head 
      while cursor is not None:
          elements.append(str(cursor._element))
          cursor = cursor._next
      return " -> ".join(elements)

  def find(self, e):
      cursor = self._head 
      while cursor is not None:
          if cursor._element == e:
              return cursor
          cursor = cursor._next

  def findPredecessor(self, e):
      predecessor = None
      cursor = self._head 
      while cursor is not None:
          if cursor._element == e:
              return predecessor, cursor
          predecessor = cursor
          cursor = cursor._next      
 
  def insert(self, insertAt, e):
      predecessor, cursor = self.findPredecessor(insertAt)
      if cursor is None:
          raise ValueError('Not in list')
          
      if predecessor is None:
          self.add_to_front(e)
      else:
          predecessor._next = self._Node(e, cursor)
          
  def delete(self, e):
      predecessor, cursor = self.findPredecessor(e)
      if cursor is None:
          raise ValueError('Not in list')
          
      if predecessor is None:
          self.remove_front()
      else:
          predecessor._next = cursor._next
          if self._tail == cursor:
              self._tail = predecessor

# Q1.1              
  def size(self):
    count = 0
    cursor = self._head
    if cursor == None:
        return count
    else:
        while cursor != None:
            count += 1
            cursor = cursor._next
    return count

# Q1.2
  def search(self, cursor, target):
    if self._size == 0:
      raise ValueError('list is empty')
    while cursor != None:
      if cursor._element == target:
        return True
      else:
        return self.search(cursor._next, target)
    return False

# Q1.3
  def second_to_last(self):
    cursor = self._head
    if self._size == 0:
        raise ValueError('list is empty')
    elif self._size == 1:
        raise ValueError('list length is one: there is no second-to-last element')
    while cursor._next != self._tail:
        cursor = cursor._next
    return cursor._element

# Q1.4
  def reverse(self):
    prev_pointer = None
    curr_pointer = self._head
    next_pointer = None
    while curr_pointer != None:
        next_pointer = curr_pointer._next
        curr_pointer._next = prev_pointer
        prev_pointer = curr_pointer
        curr_pointer = next_pointer
    self._head = prev_pointer
# the worst-case running time of this method is O(n).
# the worst-case space utilization of this method is O(1).

# Q1.5
  def second_median(self):
    slow_cursor = self._head
    fast_cursor = self._head
    while fast_cursor and fast_cursor._next:
        slow_cursor = slow_cursor._next               # slow_cursor moves by one node
        fast_cursor = fast_cursor._next._next         # fast_cursor moves by two nodes
    return slow_cursor._element

  
if __name__ == '__main__':
    ll = LinkedList()
    for i in range(5):
        ll.add_to_front(i)

    print('the given linked list is ', ll)

    ll_len = ll.size()
    print('length of ll is ', ll_len) # Q1.1

    print('is 2 in ll? ', ll.search(ll._head, 2)) # Q1.2: printing True if target is in ll, False otherwise

    print('the second-to-last element in ll is ', ll.second_to_last()) # Q1.3

    ll.reverse()
    print('ll has been reversed and now is: ', ll) # Q1.4
    ll.reverse() # returning ll to its original state

    print('the second median is ', ll.second_median()) # Q1.5