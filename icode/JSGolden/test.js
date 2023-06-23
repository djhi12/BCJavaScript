var STARTING_ITEMS_IN_INVENTORY = 20;

function start(){
    var numItems = STARTING_ITEMS_IN_INVENTORY;	

    while (numItems > 0){
        println("We have " + numItems + " items in inventory.");
		
        var numToBuy = readInt("How many would you like to buy? ");
		
        if (numToBuy <= numItems){
            numItems -= numToBuy;
            println("Now we have " + numItems + " left.");
        }else{
            println("There is not enough in inventory for that purchase.");
        }
        
        println("");
    }
    println("All Out!");
}


// Fibonacci
var MAX = 1000;

function start(){
    var first = 1;
    var second = 1;
    while(first < MAX){
        println(first);
        var third = first + second;
        first = second;
        second = third;
    }
}


























