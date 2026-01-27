<h2 class="c-project-heading--task">Pick a robot</h2>
--- task ---

Ask players to choose a robot.

--- /task ---

Add a `while` loop below to get player input. 

 

Before you start, comment out the `print` line.

<div class="c-project-code">
--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 1
line_highlights: 13, 15-16
---
# print(robots)

while True:
    robot = input("Choose a robot: ")

    if robot in robots:  # If the robot is in the dictionary then run this code
        print(robot)
    else:
        print("Robot doesn't exist!")  # If the robot doesn't exist then give an error
--- /code ---

--- task ---

**Test:** Run the code. You should see a question in the **Text output** tab.

--- /task ---

</div>

--- task ---

Test your code by entering a robot name that is in the dictionary, and one that is not.

--- /task ---

<div class="c-project-output">
<pre>Choose a robot: 
space
space
Choose a robot: 
random
Robot doesn't exist!</pre></div>