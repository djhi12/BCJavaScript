/* This program will have Karel run around the racetrack
 * 8 times. */
function start() {
    for (var i=0; i < 8; i++) {
       runLap();
   }
}

// This function has Karel run once around the track
function runLap() {
   for (var i=0; i < 4; i++) {
       runSide();
   }
}

// Karel runs one leg of the track and puts down a ball
function runSide() {
   while (frontIsClear()) {
       move();
   }
   putBall();
   turnLeft();
}