#!/usr/bin/env python3

from brain_games.game_engine import hull_of_game
from brain_games.games.brain_even import even
from brain_games.games.brain_even import rules


def main():
    hull_of_game(rules, even)


if __name__ == '__main__':
    main()
