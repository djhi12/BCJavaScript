/*
 * This program has Karel move along the first street
 * and change each blue square to be red, and each red
 * square to be blue.
 */

function start(){
    for (var i = 0; i < 9; i++) {
        invertColor();
        move();
    }
    invertColor();
}

/*
 * This function has Karel invert the color on the current space.
 * Precondition: Karel is standing on a space that is either red
 * or blue, facing East.
 * Postcondition: Karel has modified the space to be the opposite color
 * and is still standing in the same spot facing the same direction.
 */
function invertColor(){
    if (colorIs(Color.red)) {
        paint(Color.blue);
    } else {
        paint(Color.red);
    }
}