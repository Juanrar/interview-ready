# Coin Change: https://leetcode.com/problems/coin-change-ii/description/
#
# You are given an integer array coins representing coins of different denominations
# and an integer amount representing a total amount of money.
# Return the number of combinations that make up that amount.
# If that amount of money cannot be made up by any combination of the coins, return 0.
#
# Input: amount = 5, coins = [1,2,5]
# Output: 4
# Explanation: there are four ways to make up the amount:
# 5=5
# 5=2+2+1
# 5=2+1+1+1
# 5=1+1+1+1+1


def coin_change(amount: int, coins: list[int]) -> int:
    pass


# Tests


def test_returns_0_if_coins_are_invalid_or_do_not_match():
    assert coin_change(10, [15]) == 0
    assert coin_change(10, []) == 0
    assert coin_change(10, [7]) == 0


def test_returns_counts_for_various_examples():
    assert coin_change(5, [1, 2, 5]) == 4
    assert coin_change(10, [10]) == 1
