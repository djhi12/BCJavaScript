--[[
    In Lua, "\n" is a string escape sequence that represents a newline character. It is commonly used to create line breaks in strings or to format output.    
--]]

-- For example, you can use it to create a multi-line string like this:
local myString = "This is the first line.\nThis is the second line."
print(myString)

--[[
    Output:
    This is the first line.
    This is the second line.
--]]

-- In this example, the "\n" escape sequence is used to create a newline character between the two lines of text. When the string is printed to the console, the output shows the two lines on separate lines.


-- You can also use "\n" to format output, such as when printing a list of items. For example:
local myList = {"apples", "bananas", "oranges"}
for i, item in ipairs(myList) do
  print(i .. ". " .. item)
end

--[[
    Output:
    1. apples
    2. bananas
    3. oranges
--]]

-- In this example, the "\n" escape sequence is used to create a new line after each item in the list, resulting in a formatted list where each item is on its own line.