/*
    In C#, loops are used to execute a block of code repeatedly until a certain condition is met. There are several types of loops available in C#:
*/


// for loop: This loop is used to execute a block of code a specific number of times. It has three parts: initialization, condition, and iteration. The syntax of the for loop is as follows:
for (int i = 1; i <= 10; i++)
{
    Console.WriteLine(i);
}


// while loop: This loop is used to execute a block of code as long as a certain condition is true. The syntax of the while loop is as follows:
int i = 1;
while (i <= 10)
{
    Console.WriteLine(i * 2);
    i++;
}


// do-while loop: This loop is similar to the while loop, but it executes the block of code at least once before checking the condition. The syntax of the do-while loop is as follows:
int i = 1;

do
{
    Console.WriteLine(i);
    i++;
} while (i <= 10);


// foreach loop: This loop is used to iterate over a collection of items, such as an array or a list. The syntax of the foreach loop is as follows:
int[] numbers = { 1, 2, 3, 4, 5 };

// iterate over the numbers array using foreach loop
foreach (int num in numbers)
{
    Console.WriteLine(num);
}

