from LinkedListDeque import Linked_List_Deque
from ArrayDeque import Array_Deque

LL_DEQUE_TYPE = 0
ARR_DEQUE_TYPE = 1

def get_deque(deque_type=ARR_DEQUE_TYPE):
  if deque_type == LL_DEQUE_TYPE:
    return Linked_List_Deque()
  elif deque_type == ARR_DEQUE_TYPE:
    return Array_Deque()
  raise NotImplementedError