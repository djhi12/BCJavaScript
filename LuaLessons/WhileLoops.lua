--[[
    In Lua, a "while loop" is a control structure that allows a block of code to be executed repeatedly as long as a certain condition is true. The syntax for a while loop in Lua is as follows:

--]] 

while condition do
    -- code to execute while condition is true
end

-- The condition is an expression that evaluates to a boolean value (true or false). The code inside the while loop will be executed repeatedly as long as the condition is true.


-- Here's an example that demonstrates the basic usage of a while loop in Lua:
-- Print the numbers from 1 to 5 using a while loop
local i = 1
while i <= 5 do
  print(i)
  i = i + 1
end

--[[
    In this example, the condition is i <= 5, which means that the loop will continue executing as long as i is less than or equal to 5. The i variable is initialized to 1 before the loop starts, and the print(i) statement is executed in each iteration of the loop. The i = i + 1 statement increments the value of i by 1 in each iteration, so the loop will eventually terminate when i becomes greater than 5.

    It's important to ensure that the condition eventually becomes false, otherwise the loop will continue executing indefinitely, resulting in an infinite loop.    
--]]