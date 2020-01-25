# Uses python3
def edit_distance(s, t):
    n = len(s)
    m = len(t)
    
    min_dp = [[0] * (m + 1) for _ in range(n + 1)] 
    
    for i in range(1, n + 1):
        min_dp[i][0] = i
    
    for i in range(1, m + 1):
        min_dp[0][i] = i
    
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if s[i - 1] == t[j - 1]:
                min_dp[i][j] = min(min(min_dp[i - 1][j], min_dp[i][j - 1]) + 1, min_dp[i - 1][j - 1])
            else:
                min_dp[i][j] = min(min(min_dp[i - 1][j], min_dp[i][j - 1]) + 1, min_dp[i - 1][j - 1] + 1)
    
    return min_dp[n][m]

if __name__ == "__main__":
    print(edit_distance(input(), input()))
