#!/usr/bin/python3
"""
0-.Prime game
"""


def isWinner(x, nums):
    """
    define the winner of a prime game in x sessions
    """
    if x < 1 or not nums:
        return None
    maria_w, ben_w = 0, 0
    n = max(nums)
    turn = [True for _ in range(1, n + 1, 1)]
    turn[0] = False
    for i, prime_conf in enumerate(turn, 1):
        if i == 1 or not prime_conf:
            continue
        for y in range(i + i, n + 1, i):
            turn[y - 1] = False
    for _, n in zip(range(x), nums):
        n_prime = len(list(filter(lambda x: x, turn[0: n])))
        ben_w += n_prime % 2 == 0
        maria_w += n_prime % 2 == 1
    if maria_w == ben_w:
        return None
    return 'Maria' if maria_w > ben_w else 'Ben'
