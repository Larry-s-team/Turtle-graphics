import turtle as t


def draw_star(points, size, col, x, y):
   
   t.penup()
   t.goto(x, y)
   t.pendown()
   angle = 180 - (180 / points)
   t.color(col)
   t.begin_fill()
   for i in range(points):
       t.forward(size)
       t.right(angle)
   