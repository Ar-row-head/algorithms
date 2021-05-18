s1 = [10, 22, 9, 33, 21, 50, 41, 60, 80]
m = len(s1)


def lis(x, m):
    dp = [1]*(m)

    for i in range(1,m):
        for j in range(0,i):
            if x[j] < x[i]:
                dp[i] = max(dp[j]+1, dp[i])
    print(dp)
    return max(dp)

print(lis(s1, m))