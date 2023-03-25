/* Try to lay down a square of four tennis balls
 * using a for loop. */
function start(){
    for(var i = 0; i < 4; i++){
        putBall();
        move();
        turnLeft();
    }
}