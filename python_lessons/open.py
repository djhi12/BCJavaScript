"""
In Python, the open() function is used to open files in different modes. It is commonly used for reading or writing data to files. The basic syntax of the open() function is as follows:
"""

open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)

"""
Here's a breakdown of the parameters:

file: This is the name or the path of the file you want to open.

mode: This specifies the mode in which the file should be opened. The default mode is 'r' (read mode). Other common modes include 'w' (write mode), 'a' (append mode), and 'x' (exclusive creation mode). You can also specify additional options by combining modes, such as 'rb' (read mode in binary) or 'w+' (write and read mode). Refer to the documentation for a complete list of available modes.

buffering: This parameter specifies the buffering policy. The default value of -1 indicates that the system default buffering should be used.

encoding: This specifies the encoding of the file. It is optional and defaults to None, which means the system default encoding will be used.

errors: This parameter determines how errors should be handled during reading or writing. It is optional and defaults to None, which means errors will raise an exception.

newline: This parameter controls how universal newlines are handled when reading or writing text files. It is optional and defaults to None, which means universal newlines are enabled.

closefd: This specifies whether to close the file descriptor when the file is closed. It is optional and defaults to True.

opener: This is an optional custom opener that can be used to open the file. It should be a callable object.
"""

# Opening a file in read mode:
file = open('example.txt', 'r')


# Opening a file in write mode and writing data to it:
file = open('example.txt', 'w')
file.write('Hello, World!')
file.close()


# Opening a file in read mode and reading its contents:
file = open('example.txt', 'r')
content = file.read()
print(content)
file.close()

# Remember to close the file using the close() method to release system resources. Alternatively, you can use the with statement, which automatically closes the file when you're done with it:

with open('example.txt', 'r') as file:
    content = file.read()
    print(content)

# Using the with statement is considered a best practice as it ensures proper handling of file resources, even if an exception occurs.


# Example Program
# Example program to read and write data to a file

# Open a file in write mode
file = open('example.txt', 'w')

# Write data to the file
file.write('Hello, World!\n')
file.write('This is an example file.')

# Close the file
file.close()

# Open the file in read mode
file = open('example.txt', 'r')

# Read and print the contents of the file
content = file.read()
print(content)

# Close the file
file.close()

"""
In this program, we first open a file named example.txt in write mode ('w'). We then use the write() method to write two lines of text to the file. After writing the data, we close the file using the close() method.

Next, we open the same file in read mode ('r') and use the read() method to read the entire contents of the file into the content variable. Finally, we print the content of the file to the console.

Remember to replace 'example.txt' with the actual path or name of the file you want to read from or write to. Also, ensure that you have the necessary read and write permissions for the file and the correct file path.
"""