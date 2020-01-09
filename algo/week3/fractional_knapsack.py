# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    value = 0.
    val = []
    for i in range(len(weights)):
        val.append(values[i]/weights[i])
    xyz = zip(val, weights, values)
    xyz = sorted(xyz, reverse = True)
    weights_s = [y for x, y, z in xyz ]
    values_s = [z for x, y, z in xyz ]
    val_s = [x for x, y, z in xyz ]
    while capacity and len(val_s):
        if weights_s[0] <= capacity:
            value = value + weights_s[0] * val_s[0]
            capacity = capacity - weights_s[0]
            weights_s.pop(0)
            values_s.pop(0)
            val_s.pop(0)
        else:
            value = value + capacity * val_s[0]
            capacity = 0
            weights_s.pop(0)
            values_s.pop(0)
            val_s.pop(0)
    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
