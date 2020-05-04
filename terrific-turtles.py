import turtle

bob = turtle.Turtle()
#alice = turtle.Turtle()
bob.color('red')
#alice.color('blue')
bob.width(0)
#alice.width(10)

for j in range(72):
    for i in range(18):
        bob.forward(300)
        bob.right(100)
    bob.right(5)
turtle.done()