#!/usr/bin/env python3
from brain_games.logic.games_logic import game_logic_calc
from brain_games.logic.greetings import welcome


def main():
    welcome()
    game_logic_calc()


if __name__ == '__main__':
    main()
