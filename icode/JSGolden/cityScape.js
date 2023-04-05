var POLE_WIDTH = 5;
var LIGHT_RADIUS = 10;
var LIGHT_REQUIRED_HEIGHT = 200;

function start(){
	drawBuilding(50, 200, 50);
	drawBuilding(100, 300, 125);
	drawBuilding(50, 150, 200);
	drawBuilding(100, 350, 275);
}

/* Draws one building with the specified, width, height, and 
 x- coordinate. */
function drawBuilding(width, height, xPosition){
    var building = new Rectangle(width, height);
    building.setPosition(xPosition-(width/2), getHeight()-height);
    add(building);
    
    if (height>LIGHT_REQUIRED_HEIGHT) {
        var pole = new Rectangle(POLE_WIDTH,height/6);
        pole.setPosition(xPosition-(POLE_WIDTH/2), getHeight()-height-(height/6));
        add(pole);
        
        var light = new Circle(LIGHT_RADIUS);
        light.setPosition(xPosition,getHeight()-height-(height/6));
        light.setColor(Color.GREEN);
        add(light);
    }
}