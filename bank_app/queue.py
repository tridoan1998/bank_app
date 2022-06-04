 #what is the queue => data structure holds integer, has enqueue, and dequeue 
#how do we connect one node to another? 
#node1      node2     node3    <= enqueue
class Queue:
    def __init__(self, data: int, queuelist: list):
        self.data = data
        self.queuelist = queuelist

    def test_data(self):
        print(self.data)
        print(self.queuelist)

    def enqueue(self, newdata) -> int :
        self.queuelist.append(newdata)
        return None

    def dequeue(self):
        if len(self.queuelist) == 0:
            return None
        return self.queuelist.pop(0)

    def __str__(self):
        return str(self.queuelist)


def main():
    queue1 = Queue(12, [])
    queue1.enqueue(1)
    print(queue1)
    queue1.enqueue(2)
    print(queue1)
    queue1.enqueue(3)
    print(queue1)
    queue1.dequeue()
    print(queue1)
    queue1.dequeue()
    queue1.dequeue()
    print(queue1)

if __name__ == "__main__":
    main()