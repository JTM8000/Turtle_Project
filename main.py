# write program to move object foward, left, right, 90 degree turn
# use turtle module

import turtle #turtle module

#t = turtle.Turtle() #creates an object

# t.forward(100) #moves forward 100 pixels
# t.left(90) #moves left 90 degrees
# t.forward(50)
# t.backward(100)
# t.right(45)
# t.forward(200)

# exercise: create a staircase 30 pixel and 5 steps using for loop

# for i in range(0, 5):
#     t.forward(30)
#     t.left(90)
#     t.forward(30)
#     t.right(90)
# t.forward(30)

#create a function for stairs (size, nb) number of steps

t = turtle.Turtle()

def stairs(size,nb):
    size_int = 0
    nb_int = 0
    for i in range(0, nb):
        t.forward(size)
        t.left(90)
        t.forward(size)
        t.right(90)
    t.forward(size)

stairs(30,7)

#to decrement size:
# size = size - 10
# or size -= 10

turtle.done() #closes program 
