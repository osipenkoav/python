class Stationery:
    def __init__(self, t):
        self.title = t

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def __init__(self, t):
        Stationery.__init__(self, t)

    def draw(self):
        print('Pen:Запуск отрисовки')


class Pencil(Stationery):
    def __init__(self, t):
        Stationery.__init__(self, t)

    def draw(self):
        print('Pencil:Запуск отрисовки')


class Handle(Stationery):
    def __init__(self, t):
        Stationery.__init__(self, t)

    def draw(self):
        print('Handle:Запуск отрисовки')


p1 = Pen('моя ручка')
print(f'{p1.title}')
p1.draw()
pc1 = Pencil('карандашик')
print(f'{pc1.title}')
pc1.draw()
h1 = Handle('маркерочек')
print(f'{h1.title}')
h1.draw()
