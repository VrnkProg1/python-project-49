#!/usr/bin/env python3

from brain_games.game_engine import welcome_user
from brain_games.games.brain_gcd import gcd


def main():
    welcome_user(gcd)


if __name__ == '__main__':
    main()
