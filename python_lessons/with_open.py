"""
The with open statement in Python is used for opening files in a way that ensures they are properly closed after they have been used. It's the recommended way of working with files in Python because it automatically takes care of closing the file, even if an exception occurs.

The basic syntax for using with open is as follows:
"""

with open(filename, mode) as file:
    # Perform operations on the file
    print("sample")
    
"""
Here, filename is the name (and optional path) of the file you want to open, and mode specifies the purpose for which the file is being opened (e.g., read, write, append, etc.).

Within the with open block, you can perform various operations on the file object, such as reading its contents, writing to it, or manipulating its data.

Once the block is exited, either by reaching the end or encountering a return, break, or an exception, the file will be automatically closed, ensuring that any resources associated with it are released.

Here's an example that demonstrates how to read the contents of a file using with open:
"""

with open('myfile.txt', 'r') as file:
    contents = file.read()
    print(contents)

"""
In this example, the file 'myfile.txt' is opened in read mode ('r'). The read() method is then used to read the contents of the file into the contents variable, and it is subsequently printed.

Remember to adjust the file name and mode according to your specific requirements.
"""


# Example Program
filename = 'example.txt'

# Open the file in read mode and use 'with open'
with open(filename, 'r') as file:
    line_count = 0

    # Iterate over each line in the file
    for line in file:
        line_count += 1

        # Display the current line
        print(f"Line {line_count}: {line.strip()}")

# Print the total number of lines in the file
print(f"Total lines: {line_count}")

"""
In this example, we assume there is a file named 'example.txt' in the same directory as the Python script. The program opens the file in read mode ('r') using with open. It then iterates over each line in the file using a for loop and increments the line_count variable to keep track of the number of lines.

Within the loop, it prints each line after stripping any leading or trailing whitespace using the strip() method.

Finally, after the with open block is exited, the program prints the total number of lines in the file.

You can customize this program to suit your needs by modifying the file name, the operations performed on each line, or adding additional functionality.
"""