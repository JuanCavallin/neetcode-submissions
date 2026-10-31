class MyCircularQueue:

    def __init__(self, k: int):
        self.front = 0
        self.rear = 0
        self.k = k
        self.arr = [-1] * k
        

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        idx = self.rear % self.k
        self.arr[idx] = value
        self.rear += 1
        return True



    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        idx = self.front % self.k
        self.arr[idx] = -1
        self.front += 1
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        idx = self.front % self.k
        return self.arr[idx]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1        
        idx = self.rear % self.k
        return self.arr[idx - 1]
        

    def isEmpty(self) -> bool:
        return self.front == self.rear
        

    def isFull(self) -> bool:
        return abs(self.front - self.rear) == self.k


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()