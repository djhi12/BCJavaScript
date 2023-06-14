--[[
    In Lua, the keyword "local" is used to declare a variable with local scope. When you declare a variable as local, it means that the variable can only be accessed from the current block of code or function in which it is defined.    
--]]

-- Here's an example of how to declare a variable as local in Lua:
function myFunction()
    local myVariable = 10
    print(myVariable)
  end

--[[
    In this example, the variable "myVariable" is declared as local within the function "myFunction". This means that the variable can only be accessed within the function and cannot be accessed from outside the function.

    It's important to note that if you don't use the "local" keyword when declaring a variable, it will be declared as a global variable by default, and can be accessed from anywhere in your Lua program. Using local variables instead of global variables can help you avoid potential issues with variable naming conflicts and make your code easier to understand and maintain.    
--]]