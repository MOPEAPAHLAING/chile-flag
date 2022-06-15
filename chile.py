import turtle as t

for i in range(2):
    t.forward(250)
    t.left(90)
    t.forward(100)
    t.left(90)

t.fillcolor("blue")
t.begin_fill()
for i in range(4):
    t.forward(100)
    t.left(90)
t.end_fill()

t.fillcolor("red")
t.begin_fill()
for i in range(2):
    t.forward(250)
    t.right(90)
    t.forward(100)
    t.right(90)
t.end_fill()

t.penup()
t.fillcolor("white")
t.begin_fill()
t.setpos(30, 50)
for i in range(5):
    t.forward(50)
    t.right(144)
t.end_fill()

t.done()
