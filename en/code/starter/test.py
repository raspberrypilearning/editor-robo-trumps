import turtle

screen = turtle.Screen()
screen.bgcolor("white")



robots = {}

file = open("cards.txt", "r")

for line in file:
    name, battery, intelligence, image = line.strip().split(",")
    robots[name] = image
    screen.register_shape(image)


while True:
    robot = input("Choose a robot: ")

    if robot in robots:
        turtle.penup()
        turtle.goto(0, 100)
        turtle.shape(image)
    else:
        print("Robot doesn't exist!")