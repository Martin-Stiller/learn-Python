import turtle 

lines = 1_000_000


with open ("1_million_digits_of_pi.txt","r") as f:
     pi = f.read()

turtle.mode('logo')
turtle.tracer(False)
turtle.screensize(10000,10000,'black')
turtle.colormode(255)

for n in range(lines):
    color=int(n/(lines/255))
    turtle.pencolor(255,255-color,color)
    zahl = int(pi[n])
    rotation = zahl * 36
    turtle.setheading(rotation)
    turtle.forward (1)
    if n % 10_000 == 0:
        turtle.update()

turtle.getcanvas().postscript(file='PI_Picture.ps')
turtle.done()




