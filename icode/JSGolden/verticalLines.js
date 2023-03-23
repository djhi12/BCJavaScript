function start() {
    verticalLine(100, 200);
    verticalLine(200, 100);
    verticalLine(300, 20);
}

// This function draws a line starting at the
// top of the canvas at the given x
// coordinate with the given length.
function verticalLine(x, length) {
    var line = new Line(x, 0, x, length);
    add(line);
}
