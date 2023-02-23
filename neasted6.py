from turtle import*
speed('fastest')
pencolor('blue')

side=6
for i in range(side):
    fd(100)
    for i in range(side):
        fd(50)
        fillcolor('red')
        for i in range(side):   
            fd(25)
            for i in range(side):
                fd(10)
                rt(360/side)
            lt(360/side)
        rt(360/side)
    rt(360/side)

hideturtle()
mainloop()