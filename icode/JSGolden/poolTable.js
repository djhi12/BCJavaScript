var POOL_BALL_RADIUS = 40;
var POOL_BALL_FONT = "30pt Arial";

function start(){
    drawPoolBall(Color.orange, 5, 100, 100);
    drawPoolBall(Color.green, 6, 50, 200);
    drawPoolBall(Color.red, 3, 150, 350);
    drawPoolBall(Color.blue, 2, 250, 140);
}

/* Draws one pool ball with the specified color, number, and coordinates. */
function drawPoolBall(color, num, x, y){
    var poolBall = new Circle(POOL_BALL_RADIUS);
    poolBall.setColor(color);
    poolBall.setPosition(x, y);
    add(poolBall);
	
    var number = new Text(num, POOL_BALL_FONT);
    number.setColor(Color.white);
    number.setPosition(x - number.getWidth() / 2, y + number.getHeight() / 2);
    add(number);
}