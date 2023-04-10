--[[
    In Lua, insert() is a function that allows you to add a new element to a table at a specified index.    
--]]

-- The syntax for insert() is as follows:
table.insert(table, [pos,] value)

--[[
    Here, table is the table to which you want to add the element, pos is the index at which you want to insert the element, and value is the value of the element you want to insert.

    If you don't specify the pos parameter, insert() will add the element at the end of the table.
--]]

-- Here is an example of how to use insert():
fruits = {"apple", "banana", "orange"}
table.insert(fruits, 2, "grape")

-- This will insert the value "grape" at the second index position of the fruits table, shifting the other elements to the right:

{"apple", "grape", "banana", "orange"}
