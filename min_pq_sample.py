from queue import PriorityQueue

q = PriorityQueue()

q.put((227, "john smith"))
q.put((100, "tom frankson"))
q.put((99, "heidi klumm"))
q.put((109, "marvin klu"))

print(q.qsize())

print(q.get())
print(q.get())
print(q.get())

print(q.qsize())
