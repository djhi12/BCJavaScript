-- In Lua, conditional statements allow you to control the flow of your program based on whether certain conditions are true or false. The most common conditional statements in Lua are the if statement and the if-else statement.
-- The basic syntax of the if statement in Lua is as follows:
if condition then
    -- code to execute if condition is true
end

-- Here, condition is an expression that evaluates to either true or false. If condition is true, then the code block between the then and end keywords is executed. If condition is false, then the code block is skipped.

-- For example:
if x > 0 then print("x is positive") end

-- In this example, if the value of the variable x is greater than 0, then the message "x is positive" will be printed to the console.

-- The if-else statement allows you to provide an alternative code block to execute if the condition is false. The syntax is as follows:
if condition then
    -- code to execute if condition is true
else
    -- code to execute if condition is false
end

-- For example:
if x > 0 then
    print("x is positive")
else
    print("x is not positive")
end

-- In this example, if the value of x is greater than 0, then the message "x is positive" will be printed to the console. If the value of x is not greater than 0, then the message "x is not positive" will be printed instead.

-- You can also chain multiple if-else statements together using the elseif keyword:
if condition1 then
    -- code to execute if condition1 is true
elseif condition2 then
    -- code to execute if condition2 is true
else
    -- code to execute if neither condition1 nor condition2 is true
end

-- Here, if condition1 is true, then the code block after the if keyword is executed. If condition1 is false and condition2 is true, then the code block after the elseif keyword is executed. If both condition1 and condition2 are false, then the code block after the else keyword is executed.