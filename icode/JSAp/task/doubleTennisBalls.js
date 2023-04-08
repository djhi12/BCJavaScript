/* This program has Karel double a stack of balls that are one spot
 * ahead, and return to the starting position. */
function start(){
    move();
    doubleBalls();
    turnAround();
    move();
    turnAround();
}

/* This doubles a stack of balls. */
function doubleBalls(){
    while(ballsPresent()){
        takeOnePutTwoBeside();
    }
    move();

    turnAround();
    while(ballsPresent()){
        moveOneBallBack();
    }

    move();
    turnAround();
}

/* This takes one ball from a pile and puts one more ball
 * in the pile next to it. */
function moveOneBallBack(){
    takeBall();
    move();
    putBall();
    turnAround();
    move();
    turnAround();
}

/* This takes one ball from the pile and places two balls
 * in the pile next to it. */
function takeOnePutTwoBeside(){
    takeBall();
    move();
    putBall();
    putBall();
    turnAround();
    move();
    turnAround();
}