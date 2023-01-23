from queue import PriorityQueue

# implement a stack with a Priority Queue
def PQ_push(pq, myValue):
    pq.put((-1*pq.qsize(), myValue)) # time complexity of pq.qsize() is O(1)
# time complexity = O(logN)
# space complexity = O(N)

def PQ_pop(pq):
    print(pq.get()[-1])
# time complexity = O(logN)
# space complexity = O(N)

# implement a queue with a Priority Queue
def PQ_queue(pq, myValue):
    pq.put((pq.qsize(), myValue)) # time complexity of pq.qsize() is O(1)
# time complexity = O(logN)
# space complexity = O(N)

def PQ_dequeue(pq):
    print(pq.get()[-1])
# time complexity = O(logN)
# space complexity = O(N)


print("--Start of stack implementation with PQ--")
pq = PriorityQueue()
PQ_push(pq, myValue= "This is going into the stack first")
PQ_push(pq, myValue= "This is going into the stack second")
PQ_push(pq, myValue= "This is going into the stack last")
PQ_pop(pq)
PQ_pop(pq)
PQ_pop(pq)

print("--Start of queue implementation with PQ--")
newPQ = PriorityQueue()
PQ_queue(newPQ, myValue= "This is going into the queue first")
PQ_queue(newPQ, myValue= "This is going into the queue second")
PQ_queue(newPQ, myValue= "This is going into the queue last")
PQ_dequeue(newPQ)
PQ_dequeue(newPQ)
PQ_dequeue(newPQ)