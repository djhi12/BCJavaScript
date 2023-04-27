--[[
    In Lua, tostring() is a built-in function that is used to convert a Lua value to its string representation.    
--]]

local myNumber = 42
local myString = tostring(myNumber)
print(myString) -- prints "42"

--[[
    In this example, we first define a variable myNumber with the value 42. We then use the tostring() function to convert myNumber to a string and store the result in the myString variable. Finally, we print myString which will output the string "42".

    The tostring() function can be used to convert any Lua value to its string representation, including numbers, booleans, tables, functions, and more. If the value passed to tostring() is already a string, the function simply returns the same string.    
--]]

local myTable = {name = "John", age = 25}
local myTableString = tostring(myTable)
print(myTableString) -- prints "{name = \"John\", age = 25}"

-- In this example, we define a table myTable with two key-value pairs. We then use tostring() to convert myTable to a string and store the result in myTableString. Finally, we print myTableString which will output the string "{name = "John", age = 25}".