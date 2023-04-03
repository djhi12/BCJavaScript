--[[
    In Lua, a "table" is a data structure that can hold multiple values of different types, including other tables. Tables in Lua are dynamically-sized and can be used to represent arrays, dictionaries, and objects.

    Tables in Lua are created using curly braces {} and can be assigned to variables, passed as function arguments, and returned from functions. The keys in a table can be any Lua value except for nil and NaN (Not a Number), and the values can be any Lua value including other tables.

    Tables in Lua can be accessed using the index operator [], which takes the key as its argument. Tables can also be iterated over using the pairs() function, which returns a key-value pair for each entry in the table.    
--]]

-- Here's an example of creating a table in Lua:
-- create a table with some values
my_table = {1, 2, "three", {4, 5, 6}}

-- access a value in the table
print(my_table[3]) -- outputs "three"

-- iterate over the table
for key, value in pairs(my_table) do
  print(key, value)
end

--[[
    Output:
    1  1
    2  2
    3  three
    4  table: 0x7fd0f1802c50
    
--]]

-- In the example above, we created a table with four values: two numbers, a string, and another table. We then accessed the third value in the table using the index operator and printed it to the console. Finally, we iterated over the table using the pairs() function and printed each key-value pair to the console.