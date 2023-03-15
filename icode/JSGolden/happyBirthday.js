var CAKE_WIDTH = 300;
var CAKE_HEIGHT = 200;

var PLATE_WIDTH = CAKE_WIDTH + 50;
var PLATE_HEIGHT = PLATE_WIDTH/10;

var FROSTING_DROP_RADIUS = CAKE_WIDTH/24;

var CANDLE_HEIGHT = CAKE_HEIGHT/3;
var CANDLE_WIDTH = CANDLE_HEIGHT/8;
var CANDLE_WICK_HEIGHT = CANDLE_WIDTH;
var CANDLE_WICK_WIDTH = CANDLE_WIDTH/4;

function start() {

    var cake = new Rectangle(CAKE_WIDTH, CAKE_HEIGHT);
    cake.setColor(Color.ORANGE);
    cake.setPosition(getWidth()/2 - CAKE_WIDTH/2, getHeight()/2 - CAKE_HEIGHT/2);
    add(cake);
    
    var plate = new Rectangle(PLATE_WIDTH, PLATE_HEIGHT);
    plate.setColor(Color.BLUE);
    plate.setPosition(getWidth()/2 - PLATE_WIDTH/2, getHeight()/2 + CAKE_HEIGHT/2);
    add(plate);

    var numCandles = readInt("How old are you? ");
    
    for(var i = 1; i < numCandles + 1; i ++) {
        var candle = new Rectangle(CANDLE_WIDTH, CANDLE_HEIGHT);
        candle.setColor(Color.RED);
        
        if (i % 2 == 0) {
            candle.setPosition(getWidth()/2-CANDLE_WIDTH*i, cake.getY()-CANDLE_HEIGHT);
        } else {
            candle.setPosition(getWidth()/2+CANDLE_WIDTH*i, cake.getY()-CANDLE_HEIGHT);
        }
        add(candle);
    }
    
    for(var i = 0; i < 26; i += 2) {
        var frosting = new Circle(FROSTING_DROP_RADIUS);
        frosting.setColor(Color.PURPLE);
        frosting.setPosition(cake.getX() + FROSTING_DROP_RADIUS*i, cake.getY() + CAKE_HEIGHT);
        add(frosting);
    }
    
    for(var i = 0; i < 26; i += 2) {
        var frosting = new Circle(FROSTING_DROP_RADIUS);
        frosting.setColor(Color.PURPLE);
        frosting.setPosition(cake.getX() + FROSTING_DROP_RADIUS*i, cake.getY());
        add(frosting);
    }
    
    var text = new Text("Happy Birthday!", "30pt Arial");
    text.setPosition(getWidth()/2 - text.getWidth()/2, getHeight()/2 + text.getHeight()/2);
    text.setColor(Color.RED);
    add(text);
    
}