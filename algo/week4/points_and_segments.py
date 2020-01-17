# Uses python3
import collections
import sys

def fast_count_segments(starts, ends, points):
    mapp = collections.defaultdict(set)
    left_l, point_l, right_l = (1, 2, 3)
    count = [0] * len(points)
    pairs = []
    for i in starts:
        pairs.append((i, left_l))
    for i in ends:
        pairs.append((i, right_l))
    for i in range(len(points)):
        point = points[i]
        pairs.append((point, point_l))
        mapp[point].add(i)

    pairss = sorted(pairs, key=lambda p: (p[0], p[1]))

    covered = 0
    for pair in pairss:
        if pair[1] == left_l:
            covered += 1
        if pair[1] == right_l:
            covered -= 1
        if pair[1] == point_l:
            indices = mapp[pair[0]]
            for i in indices:
                count[i] = covered

    return count


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[1]
    starts = data[2:2 * n + 2:2]
    ends = data[3:2 * n + 2:2]
    points = data[2 * n + 2:]
    print(starts)
    print(ends)
    print(points)
    cnt = fast_count_segments(starts, ends, points)
    for x in cnt:
        print(x, end=" ")