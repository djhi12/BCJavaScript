--[[
    table.insert() is a built-in Lua function used to insert a new element into a table at a specified position. The function takes two parameters: the table to be modified and the value to be inserted. It can also take a third parameter, which is the position at which the value should be inserted (by default, it is inserted at the end of the table).    
--]]


-- Here is the syntax for table.insert():
table.insert(table, [pos,] value)

--[[
    table: The table to be modified.
    pos: The position at which to insert the value (optional). If not provided, the value is inserted at the end of the table.
    value: The value to be inserted.    
--]]


-- Here's an example of how to use table.insert() to add a new value to the end of a table:
local myTable = {"apple", "banana", "orange"}
table.insert(myTable, "pear")

-- myTable is now {"apple", "banana", "orange", "pear"}

-- In this example, the table.insert() function is used to add the string "pear" to the end of the myTable table.


-- You can also use table.insert() to insert a value at a specific position in the table. Here's an example:
local myTable = {"apple", "banana", "orange"}
table.insert(myTable, 2, "pear")

-- myTable is now {"apple", "pear", "banana", "orange"}

-- In this example, the table.insert() function is used to insert the string "pear" at position 2 in the myTable table. The original value at position 2 ("banana") is shifted to position 3.