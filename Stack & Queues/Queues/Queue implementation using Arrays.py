class Queue:
    def __init__(self,capacity) -> None:
        self.queue=[]
        self.front=self.rear=0
        self.size=capacity

    def Enqueue(self,data):
        if self.size==self.rear:
            print("Queue is Full")
        else:
            self.queue.append(data)
            self.rear+=1
    
    def Dequeue(self):
        if self.front==self.rear:
            print("Queue is empty")
        else:
            self.queue.pop()
            self.rear-=1
    
    def display(self):
        if self.front==self.rear:
            print("Queue is empty")
        for i in self.queue:
            print(i,"<---",end=' ')
    #print front of queue
    def frontqueue(self):
        if self.front==self.rear:
            print("Queue is empty\n")
        else:
            print("Front element of queue is ",self.queue[self.front])

if __name__=='__main__':
    q=Queue(5)
    q.frontqueue()
    q.Dequeue()
    q.Enqueue(5)
    q.Enqueue(4)
    q.Enqueue(7)
    q.Enqueue(8)
    q.Enqueue(10)
    q.Enqueue(11)
    q.Dequeue()
    q.frontqueue()
    q.display()