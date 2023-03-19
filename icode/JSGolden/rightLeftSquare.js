// ----- Right vs Left Square ------

function start() {
    if (facingNorth()) {
        makeRightSquare();
    } else {
        makeLeftSquare();
    }
}

function makeRightSquare() {
    for (var i = 0; i < 4; i++) {
        putBall();
        move();
        turnRight();
    }
}

function makeLeftSquare() {
    for (var i = 0; i < 4; i++) {
        putBall();
        move();
        turnLeft();
    }
}