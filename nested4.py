from turtle import*
speed('fastest')
pencolor('blue')

side=6
for i in range(side):
    fd(100)
    for i in range(side):
        fd(50)
        fillcolor('orange')
        begin_fill()
        for i in range(side-1):   
            fd(25)
            dot(10)
            lt(360/side-1)
        end_fill()
        rt(360/side)
    rt(360/side)

hideturtle()
mainloop()