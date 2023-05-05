var MIN_RADIUS = 20;
var MAX_RADIUS = 40;
var NUM_BALLOONS = 25;

var xPos = getWidth() / 2;
var yPos = getHeight() / 1.5;

function start() {
    for(var i = 0; i < NUM_BALLOONS; i++){
       var x = Randomizer.nextInt(MAX_RADIUS, getWidth() - MAX_RADIUS);
       var y = Randomizer.nextInt(MAX_RADIUS, getHeight()/2 - MAX_RADIUS);
      
      drawString(x, y);
      drawBalloon(x, y);
    }
}

function drawString(x, y){
    var line = new Line(xPos, yPos, x, y);
    line.setColor(Color.black);
    add(line);
}

function drawBalloon(x, y){
    var radius = Randomizer.nextInt(MIN_RADIUS, MAX_RADIUS);
    var color = Randomizer.nextColor();
    
    var balloon = new Circle(radius);
    balloon.setPosition(x, y);
    balloon.setColor(color);
    add(balloon);
}