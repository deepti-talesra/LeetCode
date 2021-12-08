# Recursive Solution
class Solution:
    def helper(self, coins, amount):
        if amount in self.memo:
            return self.memo[amount]
        min_coins_needed = float('inf')
        for coin in coins:
            if coin <= amount:
                coins_needed = self.helper(coins, amount - coin)
                min_coins_needed = min(min_coins_needed, coins_needed)
        if min_coins_needed != float('inf'):
            min_coins_needed += 1
        self.memo[amount] = min_coins_needed
        return min_coins_needed

    def coinChange(self, coins: List[int], amount: int) -> int:
        self.memo = {}
        self.memo[0] = 0
        for coin in coins:
            if coin <= amount:
                self.memo[coin] = 1
        coins.sort()
        value = self.helper(coins, amount)
        return value if value != float('inf') else -1
      
      
# Iterative Solution
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = []
        for i in range(amount + 1):
            dp.append(float('inf'))
        dp[0] = 0
        for amt in range(1, amount + 1):
            for coin in coins:
                if coin <= amt:
                    dp[amt] = min(dp[amt], dp[amt-coin]+1)
        return dp[amount] if dp[amount] != float('inf') else -1
      
      
      
