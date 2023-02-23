from turtle import*
speed('slow')
pencolor('red')

#hexagon
for i in range(6):
    fd(100)
    for i in range(6):
        fd(50)
        rt(60)
    rt(60)

hideturtle()
mainloop()