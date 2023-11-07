from DequeGenerator import get_deque

class Queue:

  def __init__(self):
  # The Big O performance is O(1). The time complexity is constant due to the method
  # only defining a variable, which is not dependent on size.
    self.__dq = get_deque()

  def __str__(self):
    # The Big O performance is O(n). The time complexity is linear due to the method
    # being dependent on size in the worst-case as it calls on str which has the 
    # complexity O(n).
    return str(self.__dq)

  def __len__(self):
    # The Big O performance is O(1). The time complexity is constant because the
    # __len__ method that is called has the complexity of O(1).
    return len(self.__dq)

  def enqueue(self, val):
    # The Big O performance is O(n). The time complexity is linear because the method
    # calls on push_back, which has a complexity of O(n) due to it being dependent on 
    # size.
    self.__dq.push_back(val)

  def dequeue(self):
    # The Big O performance is O(n). The time complexity is linear because the method
    # calls pop_front, which has a complexity of O(n) due to it being dependent on 
    # size.
    return self.__dq.pop_front()

  def peek(self):
    # The Big O performance is O(n). The time complexity is linear because the method
    # calls peek_front, which has a complexity of O(n) due to it being dependent on 
    # size.
    return self.__dq.peek_front()