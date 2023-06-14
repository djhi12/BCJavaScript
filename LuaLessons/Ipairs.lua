--[[
    In Lua, ipairs() is a built-in function that is used to iterate over an array-like table in numerical order. The ipairs() function takes a table as an argument and returns a function that can be used to iterate over the elements of the table in numerical order.    
--]]

-- Here is an example of how to use ipairs():
fruits = {"apple", "banana", "orange"}

for index, value in ipairs(fruits) do
  print(index, value)
end

--[[
    Output:
    1  apple
    2  banana
    3  orange
    
--]]

--[[
    In this example, the ipairs() function is used to iterate over the fruits table. The index variable holds the numerical index of each element in the table, and the value variable holds the corresponding value.

    It's worth noting that ipairs() only iterates over the numerical indices of a table that start from 1 and continue without any gaps. If the table has non-numerical indices or gaps in the numerical indices, ipairs() will stop iterating when it reaches the first non-numerical index or gap. To iterate over all the elements of a table, including non-numerical indices and gaps, you can use the pairs() function instead.    
--]]