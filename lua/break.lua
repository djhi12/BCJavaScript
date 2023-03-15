--[[
    In Lua, the break statement is used to exit a loop prematurely. It is often used within a loop to check for a certain condition and exit the loop if that condition is met.    
--]]

-- Here is an example of using the break statement in a while loop:
while true do
    local input = io.read()
    if input == "quit" then
      break -- exit loop
    end
    print(input)
  end

-- In this example, the loop will continue to prompt the user for input until they type "quit". When the user types "quit", the break statement is executed, and the loop is exited.


-- The break statement can also be used in a for loop. Here is an example:
for i = 1, 10 do
    if i == 5 then
      break -- exit loop
    end
    print(i)
  end

-- In this example, the loop will iterate from 1 to 10, printing the value of i each time. When i is equal to 5, the break statement is executed, and the loop is exited prematurely.