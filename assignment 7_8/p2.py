class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, data):
        self.queue.append(data)
        print(f"Enqueued: {data}")

    def dequeue(self):
        if not self.is_empty():
            removed = self.queue.pop(0)
            print(f"Dequeued: {removed}")
            return removed
        else:
            print("Queue is empty")
            return None

    def is_empty(self):
        return len(self.queue) == 0

    def display(self):
        print("Queue state:", " <- ".join(map(str, self.queue)) if self.queue else "Queue is empty")

q = Queue()
n = int(input("Enter number of elements to enqueue: "))
for _ in range(n):
    value = int(input("Enter value to enqueue: "))
    q.enqueue(value)

print("Queue after enqueue operations:")
q.display()

delete_count = int(input("Enter number of elements to dequeue: "))
for _ in range(delete_count):
    q.dequeue()

print("Queue after dequeue operations:")
q.display()
