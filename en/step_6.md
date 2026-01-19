## Display a random robot

Let’s add code so that you get a random robot when you type Random instead of a robot name.

+ First you'll need to import the choice function from the random module:

  ![screenshot](images/robotrumps-random.png)
  
+ You can use `choice` to pick a random robot name from the list of keys from the robot dictionary. 

  ![screenshot](images/robotrumps-choice.png)
  
+ In Python 3 you need to use `list` to turn the results of `keys` into a list.

  Tip: Make sure you check your brackets carefully!