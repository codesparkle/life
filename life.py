#!/usr/bin/python3

import os
import time
from functools import partial
from random import choice

from game import GameOfLife

NUM_ROWS = 30
NUM_COLS = 60

SYMBOL = {1: '██', 0: '  '}
HORIZONTAL = '━━'
VERTICAL = '│'


def main():
    game = GameOfLife(seed(NUM_ROWS, NUM_COLS))
    for generation in range(1, 200 + 1):
        clear()
        display(game.cells, generation)
        game.evolve()
        time.sleep(.01)


def seed(rows, cols, empty=False):
    make_cell = partial(choice, [True, False])
    return [[False if empty else make_cell()
             for _ in range(cols)]
            for _ in range(rows)]


def display(cells, generation):
    bar = ' ' + HORIZONTAL * NUM_COLS
    output = ['Generation {:6d}'.format(generation), bar]
    for row in cells:
        symbols = ''.join(SYMBOL[cell] for cell in row)
        output.append('{0}{1}{0}'.format(VERTICAL, symbols))
    output.append(bar)
    print('\n'.join(output))


def clear():
    os.system('clear' if os.name == 'posix' else 'cls')


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print()
