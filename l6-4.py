class Car:
    def __init__(self, s, c, n, p):
        self.name = n
        self.speed = s
        self.color = c
        self.is_police = p

    def go(self, s):
        self.speed = s
        print(f'Машина {self.name} поехала со скоростью {self.speed}')

    def stop(self):
        self.speed = 0
        print(f'Машина {self.name} остановилась. скорость = 0')

    def turn(self, d):
        print(f'Машина {self.name} повернула - {d}')

    def show_speed(self):
        print(f'Моя скорость {self.speed}')


class TownCar(Car):
    def __init__(self, s, c, n, p):
        super().__init__(s, c, n, p)

    def show_speed(self):
        print(f'TownCar: моя скорость {self.speed}')
        if self.speed > 60:
            print(f'ПРЕДУПРЕЖДЕНИЕ: скорость больше 60')


class SportCar(Car):
    def __init__(self, s, c, n, p):
        super().__init__(s, c, n, p)


class WorkCar(Car):
    def __init__(self, s, c, n, p):
        super().__init__(s, c, n, p)

    def show_speed(self):
        print(f'WorkCar: моя скорость {self.speed}')
        if self.speed > 40:
            print(f'ПРЕДУПРЕЖДЕНИЕ: скорость больше 40')


class PoliceCar(Car):
    def __init__(self, s, c, n, p):
        super().__init__(s, c, n, p)


town1 = TownCar(20, 'blue', 'ЖИГУЛЬ', False)
sport1 = SportCar(90, 'red', 'Ferrari', False)
work1 = WorkCar(50, 'green', 'Ford', False)
police1 = PoliceCar(0, 'white', 'Toyota', True)

print(f'Берем машину: {town1.name}')
town1.go(20)
town1.show_speed()
print(f'Какого цвета машина? Вот какого: {town1.color}')
town1.turn('left')
town1.go(40)
town1.show_speed()
town1.go(70)
town1.show_speed()
