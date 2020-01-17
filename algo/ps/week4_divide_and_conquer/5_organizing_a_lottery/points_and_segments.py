# Uses python3
from itertools import chain
import sys

def fast_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    #cnt = list(0*len(points))
    #write your code here
    start_tuple = zip(starts, ["l"] * len(starts))#, range(len(starts))
    print(start_tuple)
    end_tuple = zip(ends, ["r"] * len(ends))#, range(len(ends))
    print(end_tuple)
    point_tuple = zip(points, ["p"] * len(points), range(len(points)))
    print(point_tuple)
    ans = chain(start_tuple, end_tuple, point_tuple)

    ans = sorted(ans, key = lambda a: (a[0], a[1]))
    print(ans)

    count = 0
    for num, letter, index in ans:
        if letter == 'p': count += 1
        elif letter == 'r': count -= 1
        else: cnt[index] = count
    return cnt

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[1]
    starts = data[2:2 * n + 1:2]
    ends   = data[3:2 * n + 2:2]
    points = data[2 * n + 2:]
    cnt = fast_count_segments(starts, ends, points)
    for x in cnt:
        print(x, end=' ')
