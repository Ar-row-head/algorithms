x = "sunday"
y = "saturday"

lx = len(x)
ly = len(y)

def edit_word_rec(s1, s2, m, n):
    if m==0:
        return n
    if n==0:
        return m
    if s1[m-1] == s2[n-1]:
        return edit_word_rec(s1, s2, m-1, n-1)
    else:
        return min(edit_word_rec(s1, s2, m, n-1)+1, edit_word_rec(s1, s2, m-1, n-1)+1, edit_word_rec(s1, s2, m-1, n)+1)

def edit_word(s1, s2, m, n):
    dp = [[0]*(n+1) for x in range(m + 1)]
    
    for i in range(m+1):
        for j in range(n+1):
            if i==0:
                dp[i][j] = j
            elif j==0:
                dp[i][j] = i
            elif s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1+ min(dp[i][j-1], 
                                    dp[i-1][j], 
                                    dp[i-1][j-1])
    return dp[m][n]
 
    # for i in range(m + 1):
    #     for j in range(n + 1):
    #         if i == 0:
    #             dp[i][j] = j
    #         elif j == 0:
    #             dp[i][j] = i
    #         elif s1[i-1] == s2[j-1]:
    #             dp[i][j] = dp[i-1][j-1]
    #         else:
    #             dp[i][j] = 1 + min(dp[i][j-1],        # Insert
    #                                dp[i-1][j],        # Remove
    #                                dp[i-1][j-1])    # Replace
    # print(dp)
    # return dp[m][n]

def edit_word_ON(s1, s2, m, n):
    dp = [[0]*(n+1) for i in range (2)]
    for i in range(n+1):
        dp[0][i] = i
    for i in range(1,m+1):
        for j in range(n+1):
            if j==0:
                dp[i%2][j] = i
            elif s1[i-1] == s2[j-1]:
                dp[i%2][j] = dp[(i-1)%2][j-1]
            else:
                dp[i%2][j] = 1 + min(dp[i%2][j-1], dp[(i-1)%2][j], dp[(i-1)%2][j-1])
    print(dp)
    return dp[m%2][n]


print("Answer: {}".format(edit_word_rec(x, y, lx, ly)))


print("Answer in dp {}".format(edit_word(x, y, lx, ly)))

print("Answer in dp space efficient {}".format(edit_word_ON(x, y, lx, ly)))


