--[[
    In Lua, the assert() function is a built-in function that is used to check whether a given condition is true or not. If the condition is not true, the assert() function will raise an error with a specific message. 
--]] 

-- assert(condition, [message])

--[[
    Here, condition is any Lua expression that you want to check for truthfulness, and message is an optional string that you can provide to customize the error message that is displayed if the assertion fails.

    If the condition is true, assert() simply returns the value of the condition. However, if the condition is false, assert() will raise an error with the message that you provided (or a default message if no message was provided).
--]] 

local x = 10
assert(x == 5, "x is not equal to 5")

-- Example Program
-- define a function to calculate the factorial of a number
function factorial(n)
    assert(n >= 0, "n must be a non-negative integer")

    if n == 0 then
        return 1
    else
        return n * factorial(n - 1)
    end
end

-- test the factorial function with valid input
print(factorial(5)) -- output: 120

-- test the factorial function with invalid input
print(factorial(-3)) -- output: error message "n must be a non-negative integer"

--[[
    In this code, the factorial() function calculates the factorial of a non-negative integer using recursion. The assert() function is used at the beginning of the function to ensure that the input n is a non-negative integer. If the assertion fails, an error message is displayed.

    The code then tests the factorial() function with valid input (5) and invalid input (-3). When the function is called with valid input, it returns the correct result (120). However, when the function is called with invalid input, the assert() function fails and an error message is displayed (n must be a non-negative integer).    
--]]