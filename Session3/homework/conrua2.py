from turtle import *
colors = ["red", "blue", "brown", "yellow", "grey"]
for i in range(len(colors)):
    color(colors)
    begin_fill()
    for h in range(2):
        forward(50)
        left(90)
        forward(100)
        left(90)
    forward(50)
    end_fill()

    
mainloop()