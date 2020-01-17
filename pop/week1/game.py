"""
Merge function for 2048 game.
"""

def merge(line):
    """
    Function that merges a single row or column in 2048.
    """
    ans = [0]*len(line)
    pos = 0
    for num in range(len(line)):
        if line[num] != 0:
            ans[pos] = line[num]
            pos = pos + 1
    
    buff = 0
    for num in range(1,len(ans)):
        if ans[num] == ans[buff]:
            ans[buff] = str(2*ans[buff])
            ans[num] = 0
        else:
            buff = num
    ans = list(map(int, ans))
    ans = [num for num in ans if num != 0]
    add_zero = int(len(line) - len(ans))
    while add_zero:
        ans.append(0)
        add_zero = add_zero - 1
    return ans

