from turtle import*
speed('slowest')
fillcolor=('red')
begin_fill()
side=7
for i in range(side):
    fd(100)
    lt(360/side)
end_fill()
hideturtle()
mainloop()