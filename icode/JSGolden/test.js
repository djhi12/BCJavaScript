
function start(){
	var rectHeight = getHeight() / 3;
	var rectWidth = getWidth();
	
	var redRect = new Rectangle(rectWidth, rectHeight);
	redRect.setPosition(0, 0);
	redRect.setColor(Color.red);
	add(redRect);

	var blueRect = new Rectangle(rectWidth, rectHeight);
	blueRect.setPosition(0, rectHeight * 2);
	blueRect.setColor(Color.blue);
	add(blueRect);	
}

