import turtle as t

t.speed(0)
t.fillcolor("yellow")
t.begin_fill()
t.left(90)
for x in range(180):
    t.forward(1)
    t.right(1)
t.right(90)
t.forward(115)
t.end_fill()
t.fillcolor("blue")
t.begin_fill()
t.left(90)
for x in range(180):
    t.forward(1)
    t.right(1)
t.right(90)
t.forward(115)
t.end_fill()
t.fillcolor("orange")
t.begin_fill()
t.left(180)
for x in range(180):
    t.forward(1)
    t.right(1)
t.right(90)
t.forward(115)
t.end_fill()
t.fillcolor("pink")
t.begin_fill()
t.left(90)
for x in range(180):
    t.forward(1)
    t.right(1)
t.right(90)
t.forward(115)
t.end_fill()

t.done()