# python3
import sys


def compute_min_refills(distance, tank, stops):
    n = 0
    last = -1
    current = -1
    fill = -1
    stops.append(distance)
    if tank >= distance :
        return 0
    for isn in range(len(stops)) :
        if tank >= stops[isn]:
            continue
        else:
            last = isn - 1
            n = n + 1
            fill = last
            # print(stops[last])
            i = isn
            break
    while i < len(stops) :
        if last >= 0 and stops[last] + tank >= stops[i]: 
            current = i
        if last >= 0 and stops[last] + tank < stops[i] :
            last = current 
            if fill == last :
                break            
            n = n + 1
            i = i - 1
            fill = last
            # print(stops[last])
        i = i + 1
    # print(current)
    if last < 0 or current != len(stops) - 1 :
        return -1
    return n

if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, stops))
