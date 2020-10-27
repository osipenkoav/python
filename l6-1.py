from time import sleep


class TrafficLight:
    __color = ''

    def traf_switch(self, color):
        __color = color
        print(__color)
        if __color == 'red':
            sleep(7)
        elif __color == 'yellow':
            sleep(2)
        elif __color == 'green':
            sleep(5)


colors = ['red', 'yellow', 'green', 'yellow']
traf_light1 = TrafficLight()

while True:
    for c in colors:
        traf_light1.traf_switch(c)
