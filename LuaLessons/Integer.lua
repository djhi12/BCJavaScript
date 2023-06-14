--[[
    In Lua, "integer" is a primitive data type that represents whole numbers. Unlike some other programming languages, Lua does not distinguish between "integer" and "floating-point" numbers in terms of syntax, as both are represented using the same syntax for numbers.

    However, Lua provides some special operations for integers to improve performance when working with them. For example, the bitwise operators (such as bit.band and bit.bor) are optimized for integers, and may not work as expected on floating-point numbers.

    To explicitly convert a number to an integer, you can use the math.floor function, which rounds a number down to the nearest integer. For example:    
--]]

local x = 3.14
local y = math.floor(x) -- y will be 3 (an integer)

-- Note that if you try to use the modulo operator (%) with a floating-point number, Lua will first convert it to an integer using math.floor. For example:

local x = 5.6
local y = x % 2 -- y will be 1.6, not 0.6

-- If you need to work with very large integers, you may need to use a third-party library such as "lua-bigint".


-- declare some variables
local x = 5         -- an integer
local y = 2         -- another integer
local z = x + y     -- addition
local w = x - y     -- subtraction
local a = x * y     -- multiplication
local b = x / y     -- division (result will be a floating-point number)
local c = x % y     -- modulo (remainder after division)

-- print the results
print("x = " .. x)  -- use the .. operator to concatenate strings
print("y = " .. y)
print("z = " .. z)
print("w = " .. w)
print("a = " .. a)
print("b = " .. b)
print("c = " .. c)

--[[
    When you run this code, the output will be:
    x = 5
    y = 2
    z = 7
    w = 3
    a = 10
    b = 2.5
    c = 1
--]]

-- Note that the division operation (x / y) results in a floating-point number, even though both x and y are integers. If you need the result to be an integer, you can use the math.floor function to round down:

local d = math.floor(x / y)  -- integer division
print("d = " .. d)

-- This will output d = 2, which is the integer result of dividing 5 by 2.