from turtle import*
speed('fastest')
pencolor('blue')

side=6
for i in range(side):
    fd(100)
    for i in range(side):
        fd(50)
        fillcolor('red')
        begin_fill()
        for i in range(side-1):   
            fd(25)
            for i in range(side):
                fd(10)
                rt(360/side-1)
            lt(360/side)
        end_fill()
        rt(360/side)
    rt(360/side)

hideturtle()
mainloop()