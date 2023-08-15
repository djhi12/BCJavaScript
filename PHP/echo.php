<!DOCTYPE html>
<html lang="en">

    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>echo</title>
    </head>

    <body>
        <?php
    /*
        In PHP, the echo statement is used to output text or values to the browser or the client's screen. It's commonly used to display content on a webpage. Here's the basic syntax of the echo statement:
        */

    echo "Hello, world!";


    // You can also use echo to output variables, expressions, and HTML markup:
    $variable = "This is a variable.";
    echo $variable;

    $sum = 10 + 5;
    echo "The sum of 10 and 5 is: " . $sum;

    echo "<h1>This is an example of HTML markup echoed using PHP.</h1>";

    // You can use the echo statement without parentheses, as shown in the examples above. However, if you want to pass multiple values or variables to echo, you can use parentheses:

    echo ("Value 1: " . $value1 . ", Value 2: " . $value2);

    // Remember that echo is used for outputting data directly to the client's screen. If you want to capture the output as a string for further processing, you might consider using the sprintf() or printf() functions instead.


    // Example Code
    // Example 1: Basic Usage
    $name = "John";
    echo "Hello, " . $name . "!"; // Output: Hello, John!


    // Example 2: Mathematical Expression
    $number1 = 10;
    $number2 = 5;
    $sum = $number1 + $number2;
    echo "The sum of $number1 and $number2 is: " . $sum; // Output: The sum of 10 and 5 is: 15


    // Example 3: HTML Markup
    echo "<h1>Welcome to My Website</h1>";
    echo "<p>This is a paragraph of text.</p>";


    // Example 4: Escaping Characters
    $variable = "This is some \"quoted\" text.";
    echo $variable; // Output: This is some "quoted" text.


    // Example 5: Using Newlines
    $lines = "Line 1\nLine 2\nLine 3";
    echo $lines;
    // Output:
    // Line 1
    // Line 2
    // Line 3


    // Example 6: Concatenating Multiple Values
    $first_name = "Jane";
    $last_name = "Doe";
    $full_name = $first_name . " " . $last_name;
    echo "Full Name: " . $full_name; // Output: Full Name: Jane Doe


    // Example 7: Echoing HTML and PHP Together
    $variable = "PHP is powerful!";
    echo "<p>" . $variable . "</p>";

    // Remember that the echo statement is used to send output directly to the client's screen. If you're working with more complex scenarios, such as generating dynamic HTML content or handling user inputs, you might want to explore templates and frameworks to manage your code more efficiently.

    ?>
    </body>

</html>