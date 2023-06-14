--[[
    In Lua, arrays can be implemented using tables. A table in Lua can hold an ordered sequence of values, similar to an array in other programming languages.

    To create an array in Lua, you can use the table constructor syntax, which is a pair of curly braces surrounding a comma-separated list of values:    
--]]

local myArray = {10, 20, 30, 40}

-- This creates a table with four elements, which can be accessed using numeric indices:
print(myArray[1]) -- output: 10
print(myArray[2]) -- output: 20
print(myArray[3]) -- output: 30
print(myArray[4]) -- output: 40


-- You can also add or modify elements in the array using the same syntax:
myArray[2] = 25
print(myArray[2]) -- output: 25


-- In Lua, arrays can also be sparse, which means that not all indices need to have a corresponding value. You can leave gaps in the array by omitting values:
local sparseArray = {10, nil, 30, nil, 50}


-- This creates an array with five elements, but only three of them have values. You can still access the empty indices, but they will return nil:
print(sparseArray[2]) -- output: nil
print(sparseArray[4]) -- output: nil


-- You can iterate over the elements of an array using a for loop with the # operator to get the length of the array:
for i = 1, #myArray do
    print(myArray[i])
  end


--[[
    This will output:
    10
    25
    30
    40
    
--]]