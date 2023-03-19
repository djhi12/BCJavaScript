// ----- The Two Towers + Super Karel -----

// This has karel build two towers, with three balls in each tower.
// Should be the same program with turnRight and turnAround removed.
function start(){
    move();
    buildTower();
    comeDown();
    move();
    move();
    buildTower();
    move();
    turnRight();
}

// Has karel come down from the top of the tower.
// Precondition: Karel is facing north
// Postcondition: Karel is facing east at the bottom of the tower
function comeDown(){
    turnAround();
    move();
    move();
    turnLeft();
}

// This builds a three ball tower.
// Precondition: Karel is at base of tower facing east
// Postcondition: Karel has laid three balls, facing north
function buildTower(){
    turnLeft();
    putBall();
    move();
    putBall();
    move();
    putBall();
}