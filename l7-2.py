from abc import ABC, abstractmethod


class Closes(ABC):
    @abstractmethod
    def tkan_rashod(self):
        pass


class Palto(Closes):
    def __init__(self, v):
        self.V = v

    @property
    def tkan_rashod(self):
        return self.V / 6.5 + 0.5


class Suite(Closes):
    def __init__(self, h):
        self.H = h

    @property
    def tkan_rashod(self):
        return self.H * 2 + 0.3


p1 = Palto(52)
s1 = Suite(1.8)

print(f'Расход ткани для пальто: {p1.tkan_rashod}')
print(f'Расход ткани для костюма: {s1.tkan_rashod}')
