--[[
    In Lua, the pcall() function is used to execute a function in protected mode, which means that if an error occurs during the execution of the function, the error will be caught and returned as a second value to pcall(), instead of causing the program to terminate.    
--]]


-- The general syntax of pcall() is:
-- success, result1, result2, ... = pcall(function, arg1, arg2, ...)

-- where function is the function to be executed, and arg1, arg2, etc. are optional arguments to be passed to the function. success is a boolean value that indicates whether the function executed successfully or not. If success is true, result1, result2, etc. are the values returned by the function. If success is false, result1 will contain the error message.


-- Here is an example of using pcall():
function divide(a, b) 
  return a / b
end

success, result = pcall(divide, 10, 0)

if success then
  print("Result:", result)
else
  print("Error:", result)
end

-- In this example, the divide() function will cause an error if the second argument (b) is zero. By wrapping the call to divide() in pcall(), any error that occurs during the execution of divide() will be caught and returned as the second value to pcall(). The program can then check the value of success to determine whether an error occurred or not, and handle the error appropriately.


-- Example Program
-- Define a function that might raise an error
function risky_function(x)
  if x < 0 then
    error("x must be non-negative")
  end
  return math.sqrt(x)
end

-- Call the function using pcall
local success, result = pcall(risky_function, -1)

-- Check if the function executed successfully
if success then
  print("The result is:", result)
else
  print("An error occurred:", result)
end

--[[
    In this program, the risky_function() function takes a single argument x and raises an error if x is negative. We call this function using pcall() and pass in the argument -1. Since -1 is negative, we expect risky_function() to raise an error.

    After calling pcall(), we check the value of success to see if the function executed successfully. If success is true, we print the result returned by risky_function(). If success is false, we print the error message returned by pcall(). In this case, the error message is "x must be non-negative".  
--]]