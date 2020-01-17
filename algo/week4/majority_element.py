# Uses python3
import sys

def get_majority_element(a, left, right):
    maj = left
    count = 1
    for i in range(left+1, right):
        if a[maj] == a[i]:
            count += 1
        elif a[maj] != a[i]:
            count -= 1
        if count  == 0:
            maj = i
            count = 1

    count = 0
    for i in range(right):
        if a[maj] == a[i]:
            count += 1
    if count > right // 2:
        return a[maj]
    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)
