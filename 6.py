import turtle as t
k = 15
t.up()
t.tracer(0)
for x in range(-30, 30):
    for y in range(-20, 20):
        t.goto(x * k, y * k)
        t.dot(4, 'magenta')
t.speed(5)
t.tracer(1)
t.goto(20 * k, 10 * k)
t.down()
t.right(30)
for i in range(30):
    t.right(150)
    t.forward(6 * k)
    t.right(30)
    t.forward(12 * k)
t.done()

# 28