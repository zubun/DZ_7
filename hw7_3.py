
class Cell:
    def __init__(self, number, row, cell):
        self.number = number
        self.row = row
        self.cell = cell

    def __add__(self, other):
        return f'При сложении клеток {self.number} и {other.number} получилось:  {self.number + other.number} клеток'

    def __sub__(self, other):
        if self.number - other.number > 0:
            return f'При вычетании клеток {self.number} и {other.number} получилось:  {self.number + other.number} клеток'
        else:
            return 'Не возможно выполнить операцию вычетание так как разница равняется 0 !!!'
    def __mul__(self, other):
        return f'При умножении клеток {self.number} и {other.number} получилось:  {self.number * other.number} клеток'

    def __truediv__(self, other):
        return f'При делении клеток {self.number} и {other.number} получилось:  {round(self.number / other.number)} клеток'

    def make_order(self):
        all_row = self.cell / self.row
        for el in range(round(all_row)):
            print('*' * self.row)
        if self.cell - round(all_row) != 0:
            print('*' * (self.cell - (round(all_row) * self.row)))
            print('___________________')




cell_1 = Cell(10, 5, 17)
cell_2 = Cell(15, 3, 9)

print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_1 * cell_2)
print(cell_1 / cell_2)
cell_1.make_order()
cell_2.make_order()



'''В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду. Данный метод позволяет организовать ячейки по рядам.
Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно переданному аргументу. Если ячеек на формирование ряда не хватает,
 то в последний ряд записываются все оставшиеся.
Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5. Тогда метод make_order() вернет строку: *****\n*****\n**.
Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5. Тогда метод make_order() вернет строку: *****\n*****\n*****.'''