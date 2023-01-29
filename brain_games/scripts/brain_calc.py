#!/usr/bin/env python3

from brain_games.game_engine import welcome_user
from brain_games.games.brain_calc import calc


def main():
    welcome_user(calc)


if __name__ == '__main__':
    main()

