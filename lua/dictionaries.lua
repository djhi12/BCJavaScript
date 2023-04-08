--[[
    In Lua, "dictionaries" are referred to as "tables". A table is a fundamental data structure in Lua that allows you to store values of different types, such as numbers, strings, and other tables, as key-value pairs.    
--]]

-- To create a table in Lua, you can use the following syntax:
myTable = {}


-- You can then add key-value pairs to the table using the following syntax:
myTable["key"] = "value"


-- Or using shorthand syntax for keys that are valid identifiers:
myTable.key = "value"


-- You can also create a table with initial key-value pairs using the following syntax:
myTable = {key1 = "value1", key2 = "value2"}


-- To access a value in a table, you can use the key as follows:
print(myTable["key1"])  -- outputs "value1"
print(myTable.key2)     -- outputs "value2"


-- You can also iterate over the keys and values in a table using a loop, like this:
for key, value in pairs(myTable) do
    print(key .. " = " .. value)
end


-- This will output each key-value pair in the table. Note that the pairs function is used to iterate over the key-value pairs of a table in an arbitrary order. If you want to iterate over the keys in a specific order, you can use the ipairs function instead.


-- Example Code
-- create a new table and add key-value pairs
myTable = {name = "John", age = 30, hobbies = {"reading", "swimming"}}

-- print the value of a key in the table
print(myTable.name)  -- output: "John"

-- change the value of a key in the table
myTable.age = 31

-- add a new key-value pair to the table
myTable.gender = "male"

-- iterate over the keys and values in the table
for key, value in pairs(myTable) do
  if type(value) == "table" then
    -- if the value is a table, iterate over its elements
    print(key .. ": ")
    for _, elem in ipairs(value) do
      print("  - " .. elem)
    end
  else
    print(key .. ": " .. value)
  end
end

-- This code creates a table called myTable with three keys: name, age, and hobbies. The hobbies key has a value that is a table of strings. The code then prints the value of the name key, changes the value of the age key, and adds a new key-value pair to the table. Finally, the code iterates over the keys and values in the table and prints them out. If the value is a table, the code iterates over its elements and prints them out as well.