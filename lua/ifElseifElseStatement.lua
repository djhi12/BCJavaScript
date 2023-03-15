-- In Lua, you can use the if, elseif, and else keywords to create conditional statements. The basic syntax for an if statement is:

if condition then
    -- code to execute if condition is true
end


-- You can also include an else clause to execute code if the condition is false:
if condition then
    -- code to execute if condition is true
else
    -- code to execute if condition is false
end


-- To include multiple conditions, you can use elseif:
if condition1 then
    -- code to execute if condition1 is true
elseif condition2 then
    -- code to execute if condition2 is true
elseif condition3 then
    -- code to execute if condition3 is true
else
    -- code to execute if all conditions are false
end

-- Note that elseif clauses can be repeated multiple times to include as many conditions as needed.


-- Here's an example of an if statement that checks if a number is positive or negative:
local num = 10

if num > 0 then
    print("Number is positive")
elseif num < 0 then
    print("Number is negative")
else
    print("Number is zero")
end
