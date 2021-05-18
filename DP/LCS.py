s1 = "ABCDGHI"
s2 = "AEDFHRJI"

m = len(s1)
n = len(s2)

dp = [[None]*(n+1) for i in range(m+1)]

def lcs(x, y, dp, m, n):
    for i in range(m+1):
        for j in range(n+1):
            if i==0 or j==0:
                dp[i][j]=0
            elif x[i-1] == y[j-1]:
                dp[i][j] = dp[i-1][j-1]+1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp[m][n]

print(lcs(s1,s2,dp,m,n))