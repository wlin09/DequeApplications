from Deque import Deque
from LinkedList import Linked_List

class Linked_List_Deque(Deque):

  def __init__(self):
    # The Big O performance is O(1). The time complexity is constant due to
    # the method only defining self.__list, which is done in a constant number
    # of operations and is independent of size.
    self.__list = Linked_List()

  def __str__(self):
    # The Big O performance is O(1). The time complexity is constant due to
    # the method simply returning str(self.__list), which is done in a 
    # constant number of operations and not dependent on size.
    return str(self.__list)

  def __len__(self):
    # The Big O performance is O(1). The time complexity is constant due to
    # the method simply returning len(self.__list), which is done in a 
    # constant number of operations and not dependent on size.
    return len(self.__list)
  
  def push_front(self, val): 
    # The Big O performance is O(n). The time complexity is linear due to
    # the method calling insert_element_at, which has the complexity of 
    # O(n) due to having a for loop. 
    if len(self.__list) == 0:
      self.__list.append_element(val)
    else:
      self.__list.insert_element_at(val, 0)
  
  def pop_front(self): 
    # The Big O performance is O(n). The time complexity is linear due to
    # the method calling remove_element_at, which has the complexity of 
    # O(n) due to having a for loop.
    if len(self.__list) == 0:
      return None
    return self.__list.remove_element_at(0)

  def peek_front(self): 
    # The Big O performance is O(n). The time complexity is linear due to
    # the method calling get_element_at, which has the complexity of O(n)
    # due to having a for loop.
    if len(self.__list) == 0:
      return None
    return self.__list.get_element_at(0)

  def push_back(self, val): 
    # The Big O performance is O(1). The time complexity is constant due to
    # the method calling append_element, which has the complexity of O(1) due
    # to the method not having any iterations and being independent of size.
    self.__list.append_element(val)
  
  def pop_back(self): 
    # The Big O performance is O(n). The time complexity is linear due to
    # the method calling remove_element_at, which has the complexity of O(n)
    # due to having a for loop.
    if len(self.__list) == 0:
      return None
    return self.__list.remove_element_at(len(self.__list) - 1)

  def peek_back(self): 
    # The Big O performance is O(n). The time complexity is linear due to
    # the method calling get_element_at, which has the complexity of O(n)
    # due to having a for loop.
    if len(self.__list) == 0:
      return None
    return self.__list.get_element_at(len(self.__list) - 1)