from turtle import*
speed('fast')
pencolor('blue')

#hexagon
for i in range(6):
    fd(100)
    for i in range(6):
        fd(50)
        for i in range(6):    
            fd(25)
            rt(90)
        rt(60)
    rt(60)

hideturtle()
mainloop()