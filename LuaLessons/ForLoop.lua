--[[
    In Lua, a for loop has two forms:
--]] 


--[[
    Numeric for loop:
    This type of for loop iterates over a range of numbers specified by the programmer. The syntax is as follows:
--]] 

for var = start_value, end_value, increment_value do
    -- statements to be executed repeatedly
end

-- where var is the loop variable that takes values from start_value to end_value with a step size of increment_value. The increment_value is optional and defaults to 1.


-- For example, the following for loop prints the numbers from 1 to 10:
for i=1, 10 do
    print(i)
end


--[[
    Generic for loop:
    This type of for loop iterates over a set of values. The values can be returned by an iterator function. The syntax is as follows:
--]]

for var_1, ..., var_n in iterator_function do
    -- statements to be executed repeatedly
end

-- where var_1, ..., var_n are loop variables that take the values returned by the iterator_function. The iterator_function is a function that returns the values to be iterated over.


-- For example, the following for loop iterates over the elements of a table and prints them:
t = {1, 2, 3, 4, 5}
for k, v in pairs(t) do
    print(k, v)
end

-- In this example, the pairs function returns two values (the key and the value) for each element in the table, which are then assigned to the loop variables k and v, respectively.
