#!/usr/bin/env python3

from brain_games.game_engine import get_the_game_and_launch
from brain_games.games import brain_progression


def main():
    get_the_game_and_launch(brain_progression)


if __name__ == '__main__':
    main()
