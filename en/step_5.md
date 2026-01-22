<h2 class="c-project-heading--task">Add pictures</h2>
--- task ---
Make your designs come to life with pictures of your characters
--- /task ---

Show the image for your card. 

<div class="c-project-code">
--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 1
line_highlights: 5, 9-11, 13
---
for line in file.read().splitlines():
    name, battery, intelligence, image = line.split(',')  # Make into variables
    robots[name] = [battery, intelligence, image]  # Add to dictionary
    screen.register_shape(image)

print(robots)

while True:
    robot = input("Choose a robot: ")

    if robot in robots:
        print(robot)
        goto(0, 100)
        shape(stats[4])
        setheading(90)
        stamp()
        setheading(-90)
        forward(60)

    else:
        print("Robot doesn't exist!")
        

--- /code ---
--- task ---
**Test:** Run the code. Is should show the images. Add your own images by editing the code and the cards.txt file.
--- /task ---