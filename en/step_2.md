## Read robot data from a file

It's often useful to be able to read information from a file. You can then change the data in the file without having to change your code. 

+ Open this trinket: <a href="http://jumpto.cc/trumps-go" target="_blank">jumpto.cc/trumps-go</a>. 

+ Your starter project includes a `cards.txt` file which contains data about robots. 

  Click on `cards.txt` to see the data:

  ![screenshot](images/robotrumps-cards.png)

  Each line has data about a robot. The data items are separated by commas. 

  Each line contains the following information:

  name, intelligence rating, how long the battery lasts, image file name

+ Let's read the data in from the file so that you can use it. 

  The first step is to open the `cards.txt` file in your script:
  
  ![screenshot](images/robotrumps-open.png)
  
+ Now you can read the data from the file:

  ![screenshot](images/robotrumps-read.png)
  
+ You should always close a file when you have finished with it:

  ![screenshot](images/robotrumps-close.png)

+ That gives us the file as one string, you need to break it down into the individual pieces of data. 

  First, you can split the file into a list of lines:

  ![screenshot](images/robotrumps-lines.png)
  
  Look carefully at the output. There are three items in the list, each one is a line from the file. 
  
+ Now you can loop over those lines one at a time

  ![screenshot](images/robotrumps-loop.png)
  
+ Instead of printing out the lines, read them in to variables:

  ![screenshot](images/robotrumps-variables.png)
  
+ You want to be able to use this data later to look up the values for a particular robot. Let's use the robot's name as a key to a dictionary. 

  Add a `robots` dictionary:

  ![screenshot](images/robotrumps-dict.png)
  
+ Now let's add an entry to the robots dictionary for each robot. 

  The name is the key and the value is a list of data for that robot. 

  Add the highlighted code:
 
  ![screenshot](images/robotrumps-data.png)
  
  You can remove `print robots` when you have tested your script. 


