--[[
    In Lua, an "index value" usually refers to the value used to access a specific element in a table. In Lua, tables are a fundamental data structure that can be used to represent arrays, dictionaries, and objects.

    When you want to access an element in a Lua table, you can use an index value that corresponds to the position or key of the desired element. For example, if you have a Lua table that represents an array of numbers, you can access the first element by using the index value of 1, like this:    
--]]

local myArray = {10, 20, 30}
print(myArray[1]) -- prints 10

--[[
    In this example, the index value of 1 is used to access the first element of the myArray table, which is the value of 10.

    In Lua, you can use various types of values as index values, including numbers, strings, and even other tables. When you use a table as an index value, Lua uses the table's reference as a key to access the desired element in the target table.    
--]]

-- For example, consider the following code:
local myTable = {}
local key = {1, 2, 3}
myTable[key] = "Hello, World!"

print(myTable[key]) -- prints "Hello, World!"

-- In this example, a new table is created and stored in the key variable. This table is then used as an index value to access the myTable table. When Lua encounters the line myTable[key] = "Hello, World!", it uses the key table as a key to store the value of "Hello, World!" in the myTable table. When the code then prints myTable[key], Lua uses the key table again as a key to retrieve the stored value of "Hello, World!".