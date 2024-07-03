#!/usr/bin/python3
'''prime game'''


def isWinner(x, nums):
    if not nums or x < 1:
        return None

    def sieve(n):
        is_prime = [True] * (n + 1)
        p = 2
        while (p * p <= n):
            if is_prime[p] is True:
                for i in range(p * p, n + 1, p):
                    is_prime[i] = False
            p += 1
        is_prime[0], is_prime[1] = False, False
        primes = [p for p in range(n + 1) if is_prime[p]]
        return primes

    max_n = max(nums)
    primes_up_to_max_n = sieve(max_n)

    def play_game(n):
        available = [True] * (n + 1)
        turn = 0
        primes = [p for p in primes_up_to_max_n if p <= n]

        while True:
            move_made = False
            for prime in primes:
                if available[prime]:
                    move_made = True
                    for multiple in range(prime, n + 1, prime):
                        available[multiple] = False
                    break
            if not move_made:
                return 1 - turn
            turn = 1 - turn

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        winner = play_game(n)
        if winner == 0:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
