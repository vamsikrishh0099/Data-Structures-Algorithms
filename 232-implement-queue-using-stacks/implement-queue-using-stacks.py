class MyQueue:

    def __init__(self):
        self._in = []
        self.out = []

    def push(self, x: int) -> None:
        self._in.append(x)


    def pop(self) -> int:
        if not self.out:
            while self._in:
                self.out.append(self._in.pop())

        return self.out.pop()

    def peek(self) -> int:
        if not self.out:
             while self._in:
                self.out.append(self._in.pop())

        return self.out[-1]

    def empty(self) -> bool:
        return not self._in and not self.out


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()