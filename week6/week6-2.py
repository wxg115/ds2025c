from queue import Queue

q = Queue()
q.put("DataBase")
q.put("Data Structure")
q.put("Java Script")
print(q.qsize())
print(q.get())
print(q.qsize())
print(q.get())
print(q.qsize())
