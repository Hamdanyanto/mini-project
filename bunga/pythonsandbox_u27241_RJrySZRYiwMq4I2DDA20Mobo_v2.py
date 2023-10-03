import turtle

t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor('#823748')
t.pencolor('green')
t.speed(300)
col='cyan', 'yellow', 'red', 'lightgreen'
for n in range(8):
    for x in range(8):
            t.speed(x+10)
            for i in range(2):
                t.pensize(7)
                t.circle(80+n*10,90)
                t.lt(90)
            t.lt(45)
    t.pencolor(col[n%4])
s.exitonclick()
