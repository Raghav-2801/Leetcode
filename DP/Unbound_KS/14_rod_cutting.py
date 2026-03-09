price =  [1, 5, 8, 9, 10, 17, 17, 20]

def rod_cutting(price):
    n = len(price)

    dp = [[0] * (n+1) for _ in range(n+1) ]

    for i in range(1,n+1):
        for j in range(1,n+1):
            if i <= j:
                dp[i][j] = max(dp[i-1][j], price[i-1] + dp[i][j-i])
            else:
                dp[i][j] = dp[i-1][j]

    return dp[n][n]

print(rod_cutting(price))





######1D#####

def rod_cutting_1D(price):
    n = len(price)

    dp = [0] * (n+1)

    for i in range(1,n+1):
        for j in range(i,n+1):
            dp[j] = max(dp[j], price[i-1] + dp[j-i])
    return dp[n]

price =  [1, 5, 8, 9, 10, 17, 17, 20]
print(rod_cutting_1D(price))