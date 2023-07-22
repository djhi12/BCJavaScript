-- Video: https://www.youtube.com/watch?v=mJwfVC8p4P4

--[[
    In Lua, "function" is a keyword used to define a function. A function in Lua is a block of code that performs a specific task and can be called from different parts of the program.

    Here's the basic syntax for defining a function in Lua:    
--]]

function function_name(parameter1, parameter2, ...)
    -- function body
end

--[[
    In this syntax, function_name is the name of the function, and parameter1, parameter2, etc. are the parameters (or arguments) that the function expects to receive. The function body is the block of code that is executed when the function is called.

    For example, here's a simple Lua function that takes two numbers as parameters and returns their sum:    
--]]

function add_numbers(x, y)
    local result = x + y
    return result
end

-- This function can be called from anywhere in the program like this:

local sum = add_numbers(10, 20)
print(sum) -- Output: 30

-- In this example, the add_numbers function is called with the parameters 10 and 20, and the result 30 is stored in the sum variable. The print function is then used to display the value of sum on the console.


-- Example Program
-- Function to add two numbers
function add(a, b)
    return a + b
end

-- Function to subtract two numbers
function subtract(a, b)
    return a - b
end

-- Function to multiply two numbers
function multiply(a, b)
    return a * b
end

-- Function to divide two numbers
function divide(a, b)
    if b == 0 then
        return "Error: Division by zero is not allowed."
    else
        return a / b
    end
end

-- Main function
function main()
    print("Simple Calculator")
    print("------------------")
    print("Enter two numbers:")
    local num1 = tonumber(io.read())
    local num2 = tonumber(io.read())

    print("\nSelect an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    local choice = tonumber(io.read())

    local result
    if choice == 1 then
        result = add(num1, num2)
    elseif choice == 2 then
        result = subtract(num1, num2)
    elseif choice == 3 then
        result = multiply(num1, num2)
    elseif choice == 4 then
        result = divide(num1, num2)
    else
        print("Invalid choice. Please choose a valid operation (1-4).")
        return
    end

    print("Result:", result)
end

-- Run the main function
main()

--[[
To use this program, copy and paste it into a text editor and save it with a ".lua" extension (e.g., "calculator.lua"). Then, you can run the program using a Lua interpreter or an integrated development environment (IDE) that supports Lua execution.

The program will prompt you to enter two numbers and select an operation to perform (addition, subtraction, multiplication, or division). After making the choice, it will display the result of the operation. If you choose division and enter 0 as the second number, it will handle division by zero appropriately and show an error message.    
--]]