<h2 class="c-project-heading--task">Make a robots dictionary</h2>
--- task ---
Sort the robot data so you can use it in your project.
--- /task ---

Use the code below to split the data in `cards.txt` and add to a **dictionary** so that you can use it to make your trump cards.

Before you start, **comment out** the `print()` line.

<div class="c-project-code">
--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 1
line_highlights: 5, 9-11, 13
---
from turtle import *
from random import choice

robots = {}  # Define dictionary

file = open('cards.txt', 'r')
# print(file.read())  # print to test

for line in file.read().splitlines():
    name, battery, intelligence, image = line.split(',')  # Make into variables
    robots[name] = [battery, intelligence, image]  # Add to dictionary

print(robots)
--- /code ---
--- task ---
**Test:** Run the code. You should see a dictionary. Each robot name is a key, with its data stored as values.
--- /task ---

</div>
<div class="c-project-output">
<pre>{'rainbow': [' 10', ' 34', ' rainbow.png'], 'space': [' 13', ' 28', ' space.png'], 'bird': [' 6', ' 4', ' bird.png']}</pre>
</div>
