# Uses python3
import sys

def binary_search(a, x):
    l = 0
    r = len(a)-1
    while r >= l:
        m = l + (r - l) // 2
        if a[m] == x:
            return m
        elif a[m] > x:
            r = m-1
        else:
            l = m+1
    else:
        return -1

def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[n + 1]
    a = data[1 : n + 1]
    for x in data[n + 2:]:
        # replace with the call to binary_search when implemented
        print(binary_search(a, x), end = ' ')
    # print(len(a))
    # print(binary_search(a, 0, len(a)-1, 13 ))
