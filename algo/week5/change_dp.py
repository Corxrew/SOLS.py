# Uses python3
import sys

def get_change(m):
    dp_money = [100000, 1, 2, 1, 1]
    for i in range(5, m+1):
        dp_money.append(1 + min(min(dp_money[i-1], dp_money[i-3]), dp_money[i-4]))
    return dp_money[m]

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
