class Worker:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income


class Position(Worker):
    def __init__(self, name, surname, position, income):
        super().__init__(name, surname, position, income)

    def get_total_income(self):
        return self._income['wage'] + self._income['bonus']

    def get_full_name(self):
        return self.name+' '+self.surname


p = Position('Garry', 'Potter', 'survival expert', {'wage': 10000, 'bonus': 5000})

print(f'{p.get_full_name()}   {p.get_total_income()}')
