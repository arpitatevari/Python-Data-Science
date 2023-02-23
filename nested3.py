from turtle import*
speed('fastest')
pencolor('blue')

#hexagon
for i in range(6):
    pensize(5)
    fd(50)
    
    for i in range(6):
        pensize(3)
        pencolor('yellow')
        begin_fill()
        fd(50)
        for i in range(6):   
            pensize(1) 
            fd(25)
            dot(10)
            lt(60)
        end_fill()
        rt(60)
    rt(60)

hideturtle()
mainloop()