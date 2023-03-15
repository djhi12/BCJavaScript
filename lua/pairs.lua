--[[
    In Lua, pairs() is a built-in function that allows you to iterate over all key-value pairs of a table.    
--]]


-- Here's an example:
-- create a table
local myTable = {name = "John", age = 25, city = "New York"}

-- use pairs() to iterate over the table
for key, value in pairs(myTable) do
  print(key .. " = " .. value)
end

--[[
    Output:

    name = John
    age = 25
    city = New York

--]]    

-- In the example above, pairs() is used to iterate over the myTable table and print out each key-value pair. The for loop iterates over the table and for each key-value pair, assigns the key to the key variable and the value to the value variable. The print() statement then outputs the key and value concatenated together.


--[[
    Note that pairs() iterates over the table in an arbitrary order, so the output may not necessarily be in the order that the keys were added to the table.    
--]]