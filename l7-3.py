class Cell:
    def __init__(self, c):
        self.cellcount = c

    def __str__(self):
        return f'количество ячеек: {self.cellcount}'

    def __add__(self, other):
        return Cell(self.cellcount + other.cellcount)

    def __sub__(self, other):
        if self.cellcount - other.cellcount > 0:
            res = self.cellcount - other.cellcount
        else:
            print('Warning!! cells < 0 ')
            res = 0
        return Cell(res)

    def __mul__(self, other):
        return Cell(self.cellcount * other.cellcount)

    def __truediv__(self, other):
        return Cell(self.cellcount // other.cellcount)

    def make_order(self, rows):
        res = ''
        for r in range(1, self.cellcount + 1):
            res = res + '*'
            if r % rows == 0 and r >= rows:
                res = res + '\n'
        return res


cell_1 = Cell(12)
cell_2 = Cell(13)

print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_1.make_order(5))
