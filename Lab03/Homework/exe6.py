from turtle import *
from ham import draw_star
speed(0)
pencolor('blue')
for i in range(100):
    import random
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
    z = random.randint(3, 10)
    draw_star(x, y, z)

mainloop()
