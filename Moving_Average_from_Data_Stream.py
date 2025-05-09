class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.queue = deque()
        self.runningSum = 0
        

    def next(self, val: int) -> float:
        self.queue.append(val)
        self.runningSum += val
        if len(self.queue) > self.size:
            self.runningSum -= self.queue.popleft()
        return self.runningSum / len(self.queue)
