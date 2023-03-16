function start(){
    makeDiagonal();
    moveToTopMiddle();
    makeStraight();
    moveToBottomRight();
    makeDiagonal();
    moveToMiddleLeft();
    makeStraight();
    moveToCenter();
    removeExtraBalls();
}

function makeDiagonal(){
    while(frontIsClear()){
        putBall();
        move();
        turnLeft();
        move();
        turnRight();
    }
    putBall();
}

function moveToTopMiddle(){
    turnAround();
      for(var i = 0; i < 4; i++){
        move();
      }
    turnLeft();
}

function makeStraight(){
    while(frontIsClear()){
        putBall();
        move();
    }
    putBall();
}

function moveToBottomRight(){
    turnLeft();
    for(var i = 0; i < 4; i++){
        move();
    }
    turnLeft();
}

function moveToMiddleLeft(){
    turnAround();
    for (var i = 0; i < 4; i++) {
        move();
    }
    turnLeft();
}

function moveToCenter(){
    turnAround();
    for (var i = 0; i < 4; i++) {
        move();
    }
    turnAround();
}

function removeExtraBalls(){
    for(var i = 0; i < 3; i++){
        takeBall();
    }
}