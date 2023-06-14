-- Lua - "function, local, and conditional statements"

-- Function to check if a number is even or odd
function checkEvenOdd(number)
    if number % 2 == 0 then
        return "Even"
    else
        return "Odd"
    end
end

-- Function to calculate the factorial of a number
function calculateFactorial(number)
    local result = 1

    for i = 1, number do
        result = result * i
    end

    return result
end

-- Main program
print("Enter a number:")
local userInput = 20  -- Read user input and convert it to a number

-- Check if the number is even or odd
local evenOddResult = checkEvenOdd(userInput)
print(userInput .. " is " .. evenOddResult)

-- Calculate the factorial of the number
local factorialResult = calculateFactorial(userInput)
print("The factorial of " .. userInput .. " is " .. factorialResult)

--[[
In this program, the user is prompted to enter a number. The program then uses the checkEvenOdd function to determine whether the number is even or odd and prints the result. Additionally, the calculateFactorial function is used to calculate the factorial of the number and display the result. The local keyword is used to define local variables userInput, evenOddResult, and factorialResult within their respective scopes.    
--]]