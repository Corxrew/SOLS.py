# Uses python3
import sys

def get_change(m):
    deno = [10,5,1]
    count = 0
    while m:
        if m >= deno[0]:
            m = m - deno[0]
            count = count + 1
            continue
        if m >= deno[1]:
            m = m - deno[1]
            count = count + 1
            continue
        if m >= deno[2]:
            m = m - deno[2]
            count = count + 1
            continue       
    return count

if __name__ == '__main__':
    m = int(input())
    print(get_change(m))
