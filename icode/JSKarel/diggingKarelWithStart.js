function start(){
    buryBall();
    buryBall();
    buryBall();
}
    
function buryBall(){
    move();
    move();
    
    climbDown();
    putBall();
    climbUp();
    
    turnRight();
    move();
}

function climbDown(){
    turnRight();
    move();
    move();
    move();
}

function climbUp(){
    turnAround();
    move();
    move();
    move();
}
    
function turnRight(){
    turnLeft();
    turnLeft();
    turnLeft();
}

function turnAround(){
    turnLeft();
    turnLeft();
}