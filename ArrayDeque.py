from Deque import Deque

class Array_Deque(Deque):

  def __init__(self):
    # The Big O performance is O(1). The time complexity is constant because the defining of variables
    # by the method is done in a constant number of operations.
    self.__capacity = 1
    self.__contents = [None] * self.__capacity
    self.__head = 0
    self.__tail = 0
    self.__size = 0
    
  def __str__(self):
    # The Big O performance is O(n). The time complexity is linear due to the for loop, which makes the
    # number of operations dependent on size due to iterations.
    if self.__contents[self.__tail] is None:
      return "[ ]" 
    string = [str(self.__contents[(self.__head + i) % self.__capacity]) for i in range(self.__size)]
    return "[ " + ", ".join(string) + " ]" # returns proper format
    
  def __len__(self):
    # The Big O performance is O(1). The time complexity is constant due to the method only returning
    # self.__size, making the number of operations constant and independent of size.
    return self.__size

  def __grow(self):
    # The Big O performance is O(n). The time complexity is linear due to the for loop, which makes the
    # number of operations dependent on size due to iterations.
    if self.__size == self.__capacity:
      doubled_capacity = self.__capacity * 2 # doubles capacity
      new_contents = [None] * doubled_capacity
      for i in range(self.__size):
        new_contents[i] = self.__contents[(self.__head + i) % self.__capacity]
      self.__contents = new_contents
      self.__capacity = doubled_capacity
      self.__head = 0
      self.__tail = self.__size - 1
    
  def push_front(self, val):
    # The Big O performance is O(n). The time complexity is linear due to calling __grow, which has a 
    # complexity of O(n) due to a for loop.
    self.__grow()
    self.__head = (self.__head - 1) % self.__capacity
    self.__contents[self.__head] = val
    self.__size += 1 # increases size by 1
    
  def pop_front(self):
    # The Big O performance is O(1). The time complexity is constant due to the method not having any 
    # iterations, only consisting of simple operations.
    if self.__size == 0:
      return None
    pop_val = self.__contents[self.__head]
    self.__contents[self.__head] = None
    self.__head = (self.__head + 1) % self.__capacity
    self.__size -= 1 # reduces size by 1
    return pop_val
    
  def peek_front(self):
    # The Big O performance is O(1). The time complexity is constant due to the method only returning
    # self.__contents[self.__head], making the number of operations constant and independent of size.
    return self.__contents[self.__head]
    
  def push_back(self, val):
    # The Big O performance is O(n). The time complexity is linear due to calling __grow, which has a 
    # complexity of O(n) due to a for loop.
    self.__grow()
    self.__tail = (self.__tail + 1) % self.__capacity
    self.__contents[self.__tail] = val
    self.__size += 1 # increases size by 1
  
  def pop_back(self):
    # The Big O performance is O(1). The time complexity is constant due to the method not having any 
    # iterations, only consisting of simple operations.
    if self.__size == 0:
      return None
    pop_val = self.__contents[self.__tail]
    self.__contents[self.__tail] = None
    self.__tail = (self.__tail - 1) % self.__capacity
    self.__size -= 1 # reduces size by 1
    return pop_val

  def peek_back(self):
    # The Big O performance is O(1). The time complexity is constant due to the method only returning
    # self.__contents[self.__tail], making the number of operations constant and independent of size of 
    # deque.
    return self.__contents[self.__tail]