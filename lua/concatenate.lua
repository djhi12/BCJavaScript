--[[
    In Lua, concatenation is the process of joining two or more strings together to form a single string. The concatenation operator in Lua is the double dot symbol ...    
--]]

-- Here's an example of concatenating two strings in Lua:
local str1 = "Hello"
local str2 = "world"
local result = str1 .. " " .. str2
print(result) -- Output: "Hello world"

-- In this example, we first define two string variables str1 and str2. We then use the concatenation operator .. to join them together, separated by a space character, and assign the result to a new variable result. Finally, we print out the value of result, which will be the concatenated string "Hello world".


-- Note that the .. operator can be used to concatenate any type of values in Lua, not just strings. If you try to concatenate a value that is not a string, Lua will automatically convert it to a string before concatenating it. For example:

local str1 = "The answer is: "
local num = 42
local result = str1 .. num
print(result) -- Output: "The answer is: 42"

-- In this example, we concatenate a string (str1) and a number (num). Lua automatically converts the number to a string before concatenating it with str1. The result is the string "The answer is: 42".