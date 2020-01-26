# python3

import sys


class Rope:
    def __init__(self, s):
        self._ropes = s

    def result(self):
        return self._ropes

    def process(self, i, j, k):
        substring = self._ropes[i:j + 1]
        self._ropes = self._ropes[:i] + self._ropes[j + 1:]
        if k == 0:
            self._ropes = substring + self._ropes
        else:
            self._ropes = self._ropes[:k] + substring + self._ropes[k:]


rope = Rope(sys.stdin.readline().strip())
q = int(sys.stdin.readline())
for _ in range(q):
    i, j, k = map(int, sys.stdin.readline().strip().split())
    rope.process(i, j, k)
print(rope.result())