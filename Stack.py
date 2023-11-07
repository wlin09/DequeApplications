from DequeGenerator import get_deque

class Stack:

  def __init__(self):
    # The Big O performance is O(1). The time complexity is constant due to
    # the method only defining self.__dq, which is done in a constant number
    # of operations and is independent of size.
    self.__dq = get_deque()

  def __str__(self):
    # The Big O performance is O(n). The time complexity is linear because the method
    # calls on str, which has a time complexity of O(n) because it is dependent on 
    # size.
    return str(self.__dq)

  def __len__(self):
    # The Big O performance is O(1). The time complexity is constant due to
    # the method simply returning len(self.__dq), which is done in a 
    # constant number of operations and not dependent on size.
    return len(self.__dq)

  def push(self, val):
    # The Big O performance is O(n). The time complexity is linear because the method
    # calls on push_front, which has a time complexity of O(n) because it is dependent on 
    # size.
    self.__dq.push_front(val)

  def pop(self):
    # The Big O performance is O(n). The time complexity is linear because the method
    # calls on pop_front, which has a time complexity of O(n) because it is dependent on 
    # size.
    return self.__dq.pop_front()

  def peek(self):
    # The Big O performance is O(n). The time complexity is linear because the method
    # calls on peek_front, which has a time complexity of O(n) because it is dependent
    # on size.
    return self.__dq.peek_front()