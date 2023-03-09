#!/usr/bin/python3
'''Prime Game'''


def isWinner(x, nums):
    def get_primes(n):
        """
        Returns a list of primes up to and including n
        """
        sieve = [True] * (n+1)
        sieve[0] = sieve[1] = False
        for i in range(2, int(n**0.5)+1):
            if sieve[i]:
                sieve[i*i::i] = [False] * ((n-i*i)//i + 1)
        return [i for i in range(n+1) if sieve[i]]

    def play_game(n):
        """
        Returns the winner of a game played with the integers from 1 to n
        """
        primes = get_primes(n)
        if len(primes) % 2 == 0:
            return "Ben"
        else:
            return "Maria"

    wins = {"Maria": 0, "Ben": 0}

    for i in range(x):
        winner = play_game(nums[i])
        wins[winner] += 1

    if wins["Maria"] == wins["Ben"]:
        return None
    elif wins["Maria"] > wins["Ben"]:
        return "Maria"
    else:
        return "Ben"
