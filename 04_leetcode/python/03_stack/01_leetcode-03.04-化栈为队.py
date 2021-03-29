class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.pushs = []
        self.pops = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.pushs.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if not self.pops:
            self.transfer()
        return self.pops.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        if not self.pops:
            self.transfer()
        return self.pops[-1]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return not self.pushs and not self.pops

    def transfer(self) -> None:
        while self.pushs:
            self.pops.append(self.pushs.pop())

