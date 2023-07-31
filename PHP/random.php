<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>

<body>
    <?php
    $min = 1;
    $max = 100;
    $randomNumber = random_int($min, $max);

    echo "Random number between $min and $max: $randomNumber";
    ?>

</body>

</html>