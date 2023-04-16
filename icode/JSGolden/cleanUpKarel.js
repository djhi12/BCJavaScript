/* This program should clean up all the balls in any size world. */
function start() {
    while(leftIsClear()) {
        cleanRow();
        comeBack();
        moveUp();
    }
    cleanRow();
    comeBack();
    
    if (leftIsBlocked()){
        returnHome();
    }
}

/* Karel moves up to the next row.
 * Precondition: Karel is at the start of a just cleaned row.
 * Postcondition: Karel is at the start of the next row to
 * be cleaned, facing east. */
function moveUp() {
    turnLeft();
    move();
    turnRight();
}


/* This brings Karel back to the starting position on the row.
 * Precondition: Karel is at the end of the row, facing a wall.
 * Postcondition: Karel is at the start of the same row, facing
 * east.
 */
function comeBack() {
    turnAround();
    while(frontIsClear()) {
        move();
    }
    turnAround();
}

/* This cleans one row of Karel's world.
 * Precondition: Karel is at first avenue, facing east
 * Postcondition: Karel is at the end of the street, facing
 * east, and all balls in the row have been picked up.
 */
function cleanRow() {
    while(frontIsClear()) {
        cleanSpot();
        move();
    }
    cleanSpot();
}

/* This picks up a tennis ball, but only if it is there. */
function cleanSpot() {
    if(ballsPresent()) {
        takeBall();
    }
}

/* This brings Karel back to the starting position, facing east.
 * Precondition: Karel is at the end of the clean up.
 * Postcondition: Karel is back to (1,1), facing east.
 */
function returnHome(){
    turnRight();
    while(frontIsClear()){
        move();
    }
    turnLeft();
}