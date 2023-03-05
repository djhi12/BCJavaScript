"""
In Python, a string is a sequence of characters. It can be created using single quotes ('...') or double quotes ("..."). 

"""

# Here are some examples:
string1 = 'Hello, world!'
string2 = "I'm a Python string."
string3 = '''This is a
multiline
string.'''


"""
In addition to creating strings, you can perform various operations on them. Here are some common string operations in Python:

"""

# Concatenation: Joining two or more strings together using the + operator.
string1 = 'Hello'
string2 = 'world'
result = string1 + ' ' + string2
print(result)  # output: 'Hello world'


# String formatting: Replacing parts of a string with dynamic values using placeholders.
name = 'Alice'
age = 30
message = 'My name is {} and I am {} years old.'.format(name, age)
print(message)  # output: 'My name is Alice and I am 30 years old.'


# Alternatively, in Python 3.6 and later versions, you can use f-strings for string formatting:
name = 'Alice'
age = 30
message = f'My name is {name} and I am {age} years old.'
print(message)  # output: 'My name is Alice and I am 30 years old.'


# String slicing: Extracting a portion of a string using indices.
string = 'Hello, world!'
print(string[0:5])  # output: 'Hello'
print(string[7:])   # output: 'world!'


# String methods: Python provides many built-in string methods for manipulating and analyzing strings. Some common methods include lower(), upper(), strip(), replace(), split(), and join(). Here are some examples:
string = '  Hello, world!  '
print(string.lower())            # output: '  hello, world!  '
print(string.strip())            # output: 'Hello, world!'
print(string.replace('o', 'x'))  # output: '  Hellx, wxrld!  '
words = string.split(',')        # output: ['  Hello', ' world!  ']
joined = '-'.join(words)         # output: '  Hello- world!  '


