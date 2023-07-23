var COST_OF_FRISBEE = 15;
function start() {
	var numFrisbees = readInt("How many frisbees? ");
	var cost = numFrisbees * COST_OF_FRISBEE;
	println("That costs " + cost + " dollars.");
}