import turtle
turtle.reset()
#ЛИЦО
turtle.width(8)
turtle.begin_fill()
turtle.color("yellow")
turtle.circle(120)
turtle.end_fill()


turtle.up()
turtle.goto(70,70)


turtle.color("blue")
turtle.up()
turtle.goto(60,150)
turtle.begin_fill()
turtle.down()
turtle.circle(13)
turtle.end_fill()

turtle.color("white")
#зрачок
turtle.up()
turtle.goto(60,152)
turtle.begin_fill()
turtle.down()
turtle.circle(3)
turtle.end_fill()

turtle.color("blue")
turtle.up()
turtle.goto(-45,150)
turtle.begin_fill()
turtle.down()
turtle.circle(13)
turtle.end_fill()

turtle.color("white")
#зрачок
turtle.up()
turtle.goto(-45,152)
turtle.begin_fill()
turtle.down()
turtle.circle(3)
turtle.end_fill()

turtle.width(4)
turtle.up()
turtle.goto(-55,90)
turtle.down()
turtle.right(90)
turtle.color("red")
for x in range(180): 
    turtle.forward(1) 
    turtle.left(1)

turtle.color("green")
turtle.width(2)
turtle.goto(150,120)
turtle.write("Добрейшее утро")

turtle.up()
turtle.goto(0,0)
turtle.down()
turtle.right(90)
turtle.color("black")
turtle.circle(120)

turtle.up()
turtle.goto(0,0)
turtle.down()
turtle.width(6)
turtle.color("blue")
turtle.circle(125)

turtle.mainloop()


