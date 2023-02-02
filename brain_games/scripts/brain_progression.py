#!/usr/bin/env python3

from brain_games.game_engine import welcome_user
from brain_games.games.brain_progression import progression
from brain_games.games.brain_progression import rules


def main():
    welcome_user(rules, progression)


if __name__ == '__main__':
    main()
