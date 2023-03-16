function start(){
    findWall();
    findDoor();
    goToEnd();
}


function findWall(){
    turnLeft();
    goToWall();
    turnRight();
}

function findDoor(){
    while(leftIsBlocked()){
        move();
    }
}

function goToEnd(){
    turnLeft();
    goToWall();
    turnRight();
    goToWall();
}

function goToWall(){
     while(frontIsClear()){
        move();
    }
}