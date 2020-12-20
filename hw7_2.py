from abc import ABC, abstractmethod, ABCMeta


class Clothes(ABC):
    summ = []

    @abstractmethod
    def consumption_by_size(self, v):
        calculate = v / 6.5 + 0.5
        self.summ = self.summ.append(calculate)

        return calculate

    @abstractmethod
    def consumption_by_height(self, h):
        calculate = h * 2 + 0.3
        self.summ.append(calculate)
        return calculate

    @property
    def summary(self):
        return self.summ

    @summary.getter
    def summary(self):
        print(f'Сумма затраченной ткани равна: {sum(self.summ)}м')



class Coat(Clothes):
    def consumption_by_height(self, h):
        pass

    def consumption_by_size(self, v):
        print(f'Для подшивки пальто нужно: {Clothes.consumption_by_size(self, v)}м ткани')
        # print(Clothes.summ)

class Suit(Clothes):
    def consumption_by_size(self, v):
        pass

    def consumption_by_height(self, h):
        print(f'Для подшивки пальто нужно: {Clothes.consumption_by_height(self, h)}м ткани')
        # print(Clothes.summ)

coat_1 = Coat()
coat_1.consumption_by_size(6.5)
suit_1 = Suit()
suit_1.consumption_by_height(8)
suit_1.summary



