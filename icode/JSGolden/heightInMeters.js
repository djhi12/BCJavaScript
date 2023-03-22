var INCHES_TO_CM = 2.54;
var CM_TO_METERS = 0.01;
var FEET_TO_INCHES = 12;

function start(){
    convertHeightToMeters(6, 4);
    convertHeightToMeters(5, 8);
    convertHeightToMeters(5, 2);
}

// This function converts height in feet/inches
// to meters and prints the result.
function convertHeightToMeters(feet, inches) {
    var heightInInches = feet * FEET_TO_INCHES + inches;
    var heightInCentimeters = heightInInches * INCHES_TO_CM;
    var heightInMeters = heightInCentimeters * CM_TO_METERS;
    println(feet + " feet, " + inches + " inches = " + heightInMeters + " meters");
}