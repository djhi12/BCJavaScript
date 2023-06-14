--[[
    In Lua, a variable is a name that represents a value stored in computer memory. Variables are used to store and manipulate data in Lua programs.

    To create a variable in Lua, you simply need to give it a name and assign a value to it using the equals sign (=). For example, the following code creates a variable named "myVar" and assigns it the value 10:    
--]]

-- myVar = 10


--[[
    Lua is a dynamically-typed language, which means that the type of a variable is determined by the value it currently holds. You can change the value of a variable at any time, and you can assign a new value to a variable of a different type.

    Lua also has a feature called "lexical scoping", which means that the scope of a variable is determined by where it is defined in the code. A variable defined inside a function is local to that function, while a variable defined outside of any function is global to the entire program. Global variables can be accessed and modified from any part of the program, while local variables can only be accessed from within the function in which they are defined.    
--]]


-- Example Code
-- Declare a variable and assign a value
myVar = 10

-- Print the value of the variable
print(myVar)

-- Change the value of the variable
myVar = "Hello, world!"

-- Print the new value of the variable
print(myVar)

--[[
    In this example, we declare a variable named myVar and assign it the value 10. We then print the value of the variable using the print function.

    Next, we change the value of myVar to a string "Hello, world!". We then print the new value of the variable using the print function again.
--]]

-- The output of this code will be: 10 Hello, world!

-- Note that because Lua is dynamically-typed, we can change the type of myVar from a number to a string without any issues.
