def find_coins_greedy(amount, coins):
    """
    Return a dictionary of coins that make up the given amount using a greedy approach.
    Always selects the largest possible coin first.
    """
    coins = sorted(coins, reverse=True)  # ensure descending order for greedy
    result = {}
    for coin in coins:
        count = amount // coin
        if count:
            result[coin] = count
            amount -= coin * count
        if amount == 0:
            break
    return result


def find_min_coins(amount, coins):
    """
    Return a dictionary of coins that make up the given amount using dynamic programming.
    Finds the minimum total number of coins needed.
    """
    coins = sorted(coins)  # ensure ascending order for DP
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    last_coin = [0] * (amount + 1)

    for coin in coins:
        for x in range(coin, amount + 1):
            if dp[x - coin] + 1 < dp[x]:
                dp[x] = dp[x - coin] + 1
                last_coin[x] = coin

    if dp[amount] == float('inf'):
        return {}

    result = {}
    while amount > 0:
        coin = last_coin[amount]
        result[coin] = result.get(coin, 0) + 1
        amount -= coin

    return result


if __name__ == "__main__":
    coins = [50, 25, 10, 5, 2, 1]
    amount = 113

    print("Amount:", amount)
    print("Coin denominations:", coins)

    greedy_result = find_coins_greedy(amount, coins)
    dp_result = find_min_coins(amount, coins)

    print("\nGreedy algorithm result:")
    print(greedy_result)

    print("\nDynamic programming result:")
    print(dp_result)
