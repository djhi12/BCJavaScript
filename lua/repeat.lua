-- In Lua, "repeat" is a loop control structure that is used to repeatedly execute a block of code until a specified condition is met. The syntax for the "repeat" loop is as follows:


--[[
    The block of code is executed first, and then the condition is checked. If the condition is false, the block of code is executed again, and this process is repeated until the condition is true.

    It's worth noting that the "repeat" loop is similar to a "do-while" loop in other programming languages. The key difference is that in a "do-while" loop, the condition is checked at the beginning of the loop, while in a "repeat" loop, the condition is checked at the end of the loop.    
--]]

local i = 1
repeat
   print(i)
   i = i + 1
until i > 5


-- Example Program
-- Prompt the user to enter a number between 1 and 10
local num = 0
repeat
    io.write("Enter a number between 1 and 10: ")
    num = tonumber(io.read())
until num ~= nil and num >= 1 and num <= 10

-- Print out the valid number entered by the user
print("You entered the number " .. num)

-- In this program, we use the "repeat" loop to repeatedly prompt the user to enter a number between 1 and 10 until they enter a valid number. The "tonumber" function is used to convert the user's input from a string to a number, and then we check to make sure that the number is not nil (i.e., the user entered a number and not some other input) and that it falls within the range of 1 to 10. Once the user enters a valid number, we print it out using string concatenation with the "print" function.