--[[
    In Lua, a boolean is a data type that can have one of two possible values: true or false. Booleans are commonly used in programming to make decisions or to control the flow of a program.

    In Lua, the keywords true and false are used to represent boolean values. They are both considered to be constants, and their values cannot be changed during the execution of a program.    
--]]

-- Here are some examples of how booleans can be used in Lua:
-- Set a boolean variable to true
local myBoolean = true

-- Use a boolean in an if statement
if myBoolean then
  print("myBoolean is true")
else
  print("myBoolean is false")
end

-- Use a boolean in a while loop
while myBoolean do
  print("Looping!")
  myBoolean = false -- Exit the loop after one iteration
end

-- Use a boolean in a function
function myFunction(myParameter)
  if myParameter then
    print("myParameter is true")
  else
    print("myParameter is false")
  end
end

myFunction(false) -- Output: "myParameter is false"

-- Overall, booleans are a simple but essential data type in Lua programming.