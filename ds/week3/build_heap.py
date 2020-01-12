# python3
def heapify(data, i, swaps):
    smallest = i
    l = 2*i + 1
    r = 2*i + 2
    if l < len(data) and data[smallest] > data[l]:
        smallest = l
    if r < len(data) and data[smallest] > data[r]:
        smallest = r
    if smallest != i:
        swaps.append([i, smallest])
        s1 = data[i]
        data[i] = data[smallest]
        data[smallest] = s1
        heapify(data, smallest, swaps)

def build_heap(data):
    swaps = []
    start_i = int(len(data)/2 - 1)
    for i in range(start_i, -1, -1):
        heapify(data, i, swaps)
    return swaps


def main():
    n = int(input())
    data = list(map(int, input().split()))
    assert len(data) == n

    swaps = build_heap(data)

    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
