
def coin_change(coins, amount: int) -> int:
    dp = [amount+1]*(amount+1)
    dp[0] = 0
    for coin in coins:
        for i in range(coin, amount+1):
            dp[i] = min(dp[i], dp[i-coin]+1)
    return -1 if dp[amount]== amount+1 else dp[amount]

print(coin_change([3,5], 4))