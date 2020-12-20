

class Matrix:
    # x = []
    result = []
    def __init__(self, list):
        self.list = list

    def __str__(self):
        # return f'{str(self.list[0])}'
        return '\n'.join(map(str, self.list))

    # def __add__(self, other):
    #     self.result = []
    #     for el in range(len(self.list)):
    #         for i in range(len(other.list[el])):
    #             result.append(self.list[el][i] + other.list[el][i])
    #     return Matrix.__str__(self.result)

    def __add__(self, other):
        for el in range(len(self.list)):
            for i in range(len(other.list[el])):
                self.list[el][i] = (self.list[el][i] + other.list[el][i])
        return Matrix.__str__(self)


m_1 = [[1, 3, 6], [6, 9, 7], [1, 3, 8], [5, 2, 1]]
m_2 = [[5, 3, 0], [3, 0, 2], [9, 7, 2], [3, 6, 7]]
m = Matrix(m_1)
n = Matrix(m_2)
# print(m)
# print(n)
print(n + m)
