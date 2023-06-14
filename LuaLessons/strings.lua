--[[
    In Lua, strings are sequences of characters enclosed in quotes. Lua allows strings to be delimited by single quotes (') or double quotes ("), with no difference in meaning between the two.    
--]]

-- For example, the following are valid Lua strings:
"hello world"
'Lua is a powerful scripting language'
"This string contains 'quotes'"
'And this string contains "double quotes"'


-- Lua also allows multi-line strings, which are delimited by a pair of opening and closing square brackets ([[ and ]]), with any number of equal signs (=) in between, to denote the level of nesting. For example:
[[This is a
multi-line
string]]


--[[
    This will create a string containing the text "This is a\nmulti-line\nstring", where \n represents a newline character.

    Lua provides many built-in functions for working with strings, such as string.sub, string.len, string.upper, string.lower, string.find, string.match, string.gsub, and many more. These functions can be used to manipulate, search, and replace substrings within a string, as well as to convert between upper and lower case.    
--]]


-- Example Code
-- Define a string variable
local myString = "Lua is a scripting language"

-- Get the length of the string
local stringLength = string.len(myString)
print("The length of the string is:", stringLength)

-- Get a substring
local substring = string.sub(myString, 1, 3)
print("The first three characters of the string are:", substring)

-- Convert the string to uppercase
local uppercaseString = string.upper(myString)
print("The string in uppercase is:", uppercaseString)

-- Replace a substring
local replacedString = string.gsub(myString, "scripting", "powerful scripting")
print("The modified string is:", replacedString)

--[[
    This code defines a string variable myString, and then uses some of Lua's built-in string functions to manipulate it.

    First, it gets the length of the string using string.len, and prints the result to the console.

    Next, it gets the first three characters of the string using string.sub, and again prints the result.

    Then, it converts the entire string to uppercase using string.upper, and prints the result.

    Finally, it replaces the word "scripting" in the string with "powerful scripting" using string.gsub, and prints the modified string.    
--]]