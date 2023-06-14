--[[
    In Lua, a hash tag (#) is used as a length operator. It can be used to get the length of a string or the number of elements in a table.    
--]]


-- For example:
str = "Hello World"
print(#str) -- outputs: 11

myTable = {1, 2, 3, 4, 5}
print(#myTable) -- outputs: 5

-- Note that the length operator only works on sequences (i.e. tables with numeric indices starting from 1 and with no gaps). If you use it on a table that is not a sequence, it will return 0.