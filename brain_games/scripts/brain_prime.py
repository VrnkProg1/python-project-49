#!/usr/bin/env python3

from brain_games.game_engine import welcome_user
from brain_games.games.brain_prime import prime
from brain_games.games.brain_prime import rules


def main():
    welcome_user(rules, prime)


if __name__ == '__main__':
    main()
