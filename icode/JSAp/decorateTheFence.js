function start(){
    goToWall();
    turnLeft();
    decorateWall();
}

// Move along the wall
// Put a ball where there isn't a door or gate
function decorateWall(){
    while(frontIsClear()){
        if(rightIsBlocked()){
            putBall();
        }
        move();
    }
    if(rightIsBlocked()){
        putBall();
    }
}

// Go until Karel hits a wall
function goToWall(){
    while(frontIsClear()){
        move();
    }
}