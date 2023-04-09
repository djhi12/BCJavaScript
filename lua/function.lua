-- Video: https://www.youtube.com/watch?v=mJwfVC8p4P4

--[[
    In Lua, "function" is a keyword used to define a function. A function in Lua is a block of code that performs a specific task and can be called from different parts of the program.

    Here's the basic syntax for defining a function in Lua:    
--]]

function function_name(parameter1, parameter2, ...)
    -- function body
end

--[[
    In this syntax, function_name is the name of the function, and parameter1, parameter2, etc. are the parameters (or arguments) that the function expects to receive. The function body is the block of code that is executed when the function is called.

    For example, here's a simple Lua function that takes two numbers as parameters and returns their sum:    
--]]

function add_numbers(x, y)
    local result = x + y
    return result
end

-- This function can be called from anywhere in the program like this:

local sum = add_numbers(10, 20)
print(sum) -- Output: 30

-- In this example, the add_numbers function is called with the parameters 10 and 20, and the result 30 is stored in the sum variable. The print function is then used to display the value of sum on the console.