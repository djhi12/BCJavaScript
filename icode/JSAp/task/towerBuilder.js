/* This program will have Karel build a tower on
 * every odd avenue. A tower consists of 3 tennis balls
 * stacked on top of each other. */
function start() {
    buildTower();
    while(frontIsClear()){
        move();
        if(frontIsClear()){
            move();
            buildTower();
        }
    }
}

/* This function has Karel build a tower that is three balls high.
 * Precondition: Karel is facing east at the location to build the tower.
 * Postcondition: Karel has built the tower, and is back at the base
 *                facing east.
 */
function buildTower(){
    turnLeft();
    for(var i = 0; i < 3; i++){
        putBall();
        move();
    }
    turnAround();
    goDown();
    turnLeft();
}

/* This function moves Karel to the wall. */
function goDown(){
    while(frontIsClear()){
        move();
    }
}