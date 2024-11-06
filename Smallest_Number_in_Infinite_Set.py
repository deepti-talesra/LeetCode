class SmallestInfiniteSet:

    def __init__(self):
        self.smallest = 1
        self.removed = set()

    def popSmallest(self) -> int:
        ret = self.smallest
        self.removed.add(ret)
        self.smallest += 1
        while self.smallest in self.removed:
            self.smallest += 1
        return ret

    def addBack(self, num: int) -> None:
        if num in self.removed:
            self.removed.remove(num)
            if num < self.smallest:
                self.smallest = num
