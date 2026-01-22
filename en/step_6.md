<h2 class="c-project-heading--task">Display the text</h2>
--- task ---
Add text to your image
--- /task ---

<div class="c-project-code">
--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 1
line_highlights: 5, 9-11, 13
---
  if robot in robots:
    stats = robots[robot]
    style = ('Courier', 14, 'bold')
    clear()
    color(stats[5])
    goto(0, 100)
    shape(image)
    setheading(90)
    stamp()
    setheading(-90)
    forward(60)
    write('Name: ' + robot, font=style, align='center')
    forward(25)
    write('Battery: ' + battery, font=style, align='center')
    forward(25)
    write('Intelligence: ' + intelligence, font=style, align='center')
    forward(25)

--- /code ---
--- task ---
**Test:** Run the code. Is should show the images. Add your own images by editing the code and the cards.txt file.
--- /task ---
    
Style the name. You can Change the font. Instead of `Arial` you could try: `Courier`, `Times` or `Verdana`. 

Change `14` to a different number to change the size of the font. 

You can change `bold` to `normal` or `italic`. 
  
  