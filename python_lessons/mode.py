"""
The available modes for opening a file are:

'r': Read mode (default). Opens a file for reading.
'w': Write mode. Opens a file for writing. Creates a new file if it doesn't exist or truncates the file if it exists.
'x': Exclusive creation mode. Opens a file for exclusive creation. Fails if the file already exists.
'a': Append mode. Opens a file for appending data. Creates a new file if it doesn't exist.
'b': Binary mode. Opens a file in binary mode.
't': Text mode (default). Opens a file in text mode.

You can combine different modes by concatenating them. For example, 'rb' opens a file in binary mode for reading.

Once you open a file using the "with open" statement, you can perform various operations on the file, such as reading its contents, writing data to it, or manipulating its contents. When the code execution leaves the "with" block, the file is automatically closed, ensuring proper cleanup.
"""