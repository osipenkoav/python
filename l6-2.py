class Road:
    def __init__(self, len, wid):
        self._length = len
        self._width = wid

    def massa_asf(self):
        return self._length*self._width*25*5

r = Road(5000, 20)

#print(str(r._length), str(r._width))
print(f'Масса асфальта: {r.massa_asf()//1000} тонн')