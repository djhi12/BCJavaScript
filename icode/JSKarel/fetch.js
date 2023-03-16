/* This program has Karel fetch a ball and come back. */
function start() {
    goToBall();
    takeBall();
    turnAround();
    comeBack();
    turnAround();
    putBall();
}

// This program takes Karel to the tennis ball.
function goToBall() {
    moveUpAndRight();
}

// This moves Karel to the starting position.
function comeBack() {
    moveUpAndRight();
}

// This function has Karel move in a zig zag shape up
// four spaces and to the right
function moveUpAndRight() {
    move();
    turnLeft();
    move();
    move();
    move();
    move();
    turnRight();
    move();
}