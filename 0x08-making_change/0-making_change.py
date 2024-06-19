#!/usr/bin/python3
"""
Given a pile of coins of different values, determine the fewest number
of coins needed to meet a given amount total.

 - Prototype: def makeChange(coins, total)
 - Return: fewest number of coins needed to meet total
           If total is 0 or less, return 0
           If total cannot be met by any number of coins you have, return -1

coins is a list of the values of the coins in your possession
The value of a coin will always be an integer greater than 0
assume you have an infinite number of each denomination of coin in the list
solution’s runtime will be evaluated
"""


def makeChange(coins, total):
    """ greedy algorithm """
    if total <= 0:
        return 0
    n_coin, plus = 0, 0

    coins.sort()
    coins = coins[::-1]
    while len(coins) > 0:
        amount = coins[0]
        if plus + amount > total:
            coins.pop(0)
            continue
        plus += amount
        n_coin += 1
        if plus == total:
            return n_coin
    return -1
