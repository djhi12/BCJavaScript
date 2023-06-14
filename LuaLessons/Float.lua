--[[
    In Lua, there is no data type specifically called "float". Instead, Lua has a single numerical data type called "number", which is a floating-point type that can represent both integer and non-integer values.

    When you perform arithmetic operations on two "number" values, Lua automatically converts the result to a "number" value. For example:    
--]]

local x = 3.14 -- x is a "number" value
local y = 2 -- y is also a "number" value
local z = x + y -- z is a "number" value, equal to 5.14

-- If you need to explicitly specify a floating-point number, you can append a decimal point to the value:

local a = 3.0 -- a is a "number" value, equal to 3.0
local b = 1.5 -- b is a "number" value, equal to 1.5

-- It's worth noting that Lua uses double-precision floating-point numbers to represent "number" values, which provides a range of approximately ±1.7e308 and a precision of about 15 decimal places.


-- initialize some "number" variables
local x = 2
local y = 3.14

-- perform arithmetic operations
local sum = x + y
local difference = x - y
local product = x * y
local quotient = x / y

-- print the results
print("The sum of", x, "and", y, "is", sum)
print("The difference between", x, "and", y, "is", difference)
print("The product of", x, "and", y, "is", product)
print("The quotient of", x, "and", y, "is", quotient)

--[[
    Output:
    The sum of	2	and	3.14	is	5.14
    The difference between	2	and	3.14	is	-1.14
    The product of	2	and	3.14	is	6.28
    The quotient of	2	and	3.14	is	0.63694267515924

    
    In this example, we initialize two variables, x and y, with the values of 2 and 3.14, respectively. We then perform several arithmetic operations using these variables, such as addition, subtraction, multiplication, and division, and store the results in separate variables. Finally, we print the results to the console using the print() function.
    
--]]