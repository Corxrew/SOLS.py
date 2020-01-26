# python3

import sys
import threading

sys.setrecursionlimit(10 ** 6)  # max depth of recursion
threading.stack_size(2 ** 27)  # new thread will get stack of such size

class TreeOrders:

    def read(self):
        self.n = int(sys.stdin.readline())
        self.key = [0 for _ in range(self.n)]
        self.left = [0 for _ in range(self.n)]
        self.right = [0 for _ in range(self.n)]
        for i in range(self.n):
            self.key[i], self.left[i], self.right[i] = map(
                int, sys.stdin.readline().split()
            )

    def in_order(self):
        c_id = 0
        stack_order = []

        while True:
            if c_id != -1:
                stack_order.append(c_id)
                c_id = self.left[c_id]
            elif stack_order:
                c_id = stack_order.pop()
                yield self.key[c_id]
                c_id = self.right[c_id]
            else:
                break

    def pre_order(self):
        c_id = 0
        stack_order = []

        while True:
            if c_id != -1:
                yield self.key[c_id]
                stack_order.append(c_id)
                c_id = self.left[c_id]
            elif stack_order:
                c_id = stack_order.pop()
                c_id = self.right[c_id]
            else:
                break

    def post_order(self):
        stack_order1 = [0]
        stack_order2 = []

        while stack_order1:
            c_id = stack_order1.pop()
            stack_order2.append(self.key[c_id])

            left_id = self.left[c_id]
            right_id = self.right[c_id]
            if left_id != -1:
                stack_order1.append(left_id)
            if right_id != -1:
                stack_order1.append(right_id)

        while stack_order2:
            yield stack_order2.pop()


def main():
    tree = TreeOrders()
    tree.read()
    print(" ".join(str(x) for x in tree.in_order()))
    print(" ".join(str(x) for x in tree.pre_order()))
    print(" ".join(str(x) for x in tree.post_order()))


threading.Thread(target=main).start()
