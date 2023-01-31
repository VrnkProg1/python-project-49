#!/usr/bin/env python3

from brain_games.game_engine import welcome_user
from brain_games.games.brain_calc import calc
from brain_games.games.brain_calc import rules


def main():
    welcome_user(rules, calc)


if __name__ == '__main__':
    main()

