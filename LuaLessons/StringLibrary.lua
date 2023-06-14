--[[
    Lua has a built-in "string library" that provides a collection of functions for working with strings. Here are some of the commonly used functions in the string library:

        string.sub(s, i, j): This function returns the substring of the string 's' from index 'i' to index 'j'. If 'j' is not provided, it returns the substring from 'i' to the end of the string.

        string.len(s): This function returns the length of the string 's'.

        string.rep(s, n): This function returns a new string which is a concatenation of 'n' copies of the string 's'.

        string.lower(s): This function returns a new string which is a copy of the string 's' in lowercase.

        string.upper(s): This function returns a new string which is a copy of the string 's' in uppercase.

        string.find(s, pattern, start, plain): This function searches the string 's' for the first occurrence of the pattern 'pattern'. If found, it returns the indices of the first and last characters of the match. If not found, it returns nil. 'start' and 'plain' are optional arguments that can be used to specify the starting index of the search and whether the pattern is a plain string or a pattern.

        string.gsub(s, pattern, replace, n): This function searches the string 's' for all occurrences of the pattern 'pattern' and replaces them with 'replace'. 'n' is an optional argument that can be used to specify the maximum number of replacements to make.

        string.match(s, pattern, start): This function searches the string 's' for the first occurrence of the pattern 'pattern' and returns the captures of the match. If 'start' is provided, the search starts at that index.

        string.reverse(s): This function returns a new string which is a copy of the string 's' with its characters in reverse order.

    These are just some of the functions available in the string library. There are many more functions that you can use to manipulate strings in Lua.    
--]]

-- Define a string
local myString = "Hello World"

-- Get the length of the string
local stringLength = string.len(myString)
print("The length of the string is:", stringLength)

-- Get a substring of the string
local subString = string.sub(myString, 7)
print("The substring of the string is:", subString)

-- Convert the string to uppercase
local upperString = string.upper(myString)
print("The uppercase string is:", upperString)

-- Replace all occurrences of a pattern in the string
local replacedString = string.gsub(myString, "l", "x")
print("The replaced string is:", replacedString)

-- In this code, we define a string "Hello World" and then use the string library functions to get the length of the string, extract a substring from the string, convert the string to uppercase, and replace all occurrences of a pattern in the string. We then print out the results of each operation.