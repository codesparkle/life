from copy import deepcopy

DELTA = (-1, 0, 1)


class GameOfLife:
    def __init__(self, cells):
        self.cells = cells

    def evolve(self):
        new_iteration = deepcopy(self.cells)
        for i, row in enumerate(self.cells):
            for j, _ in enumerate(row):
                r, c = self.get_row(i), self.get_col(j)
                live_neighbours = self.sum_of_block(i, j)
                if live_neighbours == 3:
                    new_iteration[r][c] = True
                elif live_neighbours != 4:
                    new_iteration[r][c] = False

        self.cells = new_iteration

    def sum_of_block(self, row, col):
        return sum(self.get_cell(row + i, col + j)
                   for i in DELTA
                   for j in DELTA)

    def get_cell(self, row, col):
        return self.cells[self.get_row(row)][(self.get_col(col))]

    def get_row(self, row):
        return row % len(self.cells)

    def get_col(self, col):
        return col % len(self.cells[0])
