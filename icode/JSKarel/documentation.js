Karel's Built in Commands
Commands
move();
JavaScript
 	
turnLeft();
JavaScript
turnRight();
JavaScript
 	
turnAround();
JavaScript
putBall();
JavaScript
 	
takeBall();
JavaScript
UltraKarel Commands
paint(color);
JavaScript
 
UltraKarel Conditions
randomChance();
JavaScript
 	
colorIs(color);
JavaScript
// Paints a square red.
paint(Color.red);

Colors:

Color.red
Color.blue
Color.green
Color.yellow
Color.cyan
Color.orange
Color.white
Color.black
Color.gray
Color.purple

// Special Random color function
Color.random()

// Paint a square a random color
paint(Color.random());

// Determine if a square is a certain color
if(colorIs(Color.red)){
    move();
}

// Create a color from RGB to paint this square
// paint(Color.createFromRGB(redValue, greenValue, blueValue));
paint(Color.createFromRGB(12, 14, 19));


Random

// Returns true 50% of the time
randomChance()

// Returns true probability percentage of the time
randomChance(probability)

// Returns true 20% of the time.
randomChance(0.2)


// Example
if (randomChance(0.8)) {
    putBall();
}
JavaScript
Functions
Writing a Function
Writing a function is like teaching karel a new word.

Naming Functions: You can name your functions whatever you want, but you can't have spaces in the function name.

Remember that each open bracket { must match with a close bracket }

function turnRight() {
    turnLeft();
    turnLeft();
    turnLeft();
}

function turnAround() {
    turnLeft();
    turnLeft();
}

function yourFunctionName() {
  // Code that will run when you make a call to
  // this function.
}
JavaScript
Conditional Statements
If Statements
Remember that each open bracket { must match with a close bracket }
if (condition) {
  // code that will run if the condition is true
}
JavaScript
if (condition) {
  // code that will run if the condition is true
} else {
  // code that will run if condition is not true
}
JavaScript
Example of if statements
if (frontIsClear()) {
    move();
}

if (ballsPresent()) {
    takeBall();
} else {
    move();
}
JavaScript
Karel Conditions
Don't forget the () at the end
frontIsClear()
leftIsClear()
rightIsClear()

facingNorth()
facingSouth()
facingEast()
facingWest()

ballsPresent()
            
JavaScript
 	
frontIsBlocked()
leftIsBlocked()
rightIsBlocked()

notFacingNorth()
notFacingSouth()
notFacingEast()
notFacingWest()

noBallsPresent()
            
JavaScript
Loops
Remember that each open bracket { must match with a close bracket }
While Loops
while (CONDITION) {
  // Code that will run while the CONDITION is true.
  // Once the CONDITION is no longer true,
  // it will stop.
}
JavaScript
Example of while loops
/* This moves Karel to a wall */
while (frontIsClear()) {
    move();
}


//For Loops
for (var i = 0; i < COUNT; i++) {
  // Code that will run 'COUNT' times
}


// Example of for loops
/* This puts down 10 balls */
for (var i = 0; i < 10; i++) {
    putBall();
}

// You can have multiple statements or function calls in a for loop.
/* This puts down five balls and
   moves after each one */
for (var i = 0; i < 5; i++) {
    putBall();
    move();
}
JavaScript
Use for-loops when you want to repeat something a fixed number of times.
Use while-loops when you want to repeat something as long as a condition is true.
Comments
Comments
/* A multi-line comment describes your code
 * to someone who is reading it. */

// Use single line comments to clarify code.