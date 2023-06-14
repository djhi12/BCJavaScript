--[[
    In Lua, a "tuple" is a collection of values of different types that are stored together in a single variable. However, unlike tables, tuples are immutable, meaning that their values cannot be changed once they are created.
-]]

-- To create a tuple in Lua, you can simply use parentheses to enclose the values, like this:
local myTuple = (1, "hello", true)

-- In this example, myTuple is a tuple that contains an integer value (1), a string value ("hello"), and a boolean value (true).


-- You can access individual values in a tuple using the indexing operator, like this:
local myNumber = myTuple[1]
local myString = myTuple[2]
local myBoolean = myTuple[3]


--[[
    In this case, myNumber would be set to 1, myString would be set to "hello", and myBoolean would be set to true.

    It's worth noting that while tuples are not as versatile as tables in Lua, they can be useful for certain tasks, such as returning multiple values from a function or grouping related values together.    
--]]


-- Example Code
local person = ("John", "Doe", 30)
print("Name: " .. person[1] .. " " .. person[2])
print("Age: " .. person[3])

--[[
    In this example, we create a tuple called person that contains three values: the person's first name ("John"), last name ("Doe"), and age (30).

    We then use the indexing operator to access the individual values in the tuple and print them to the console. The .. operator is used to concatenate strings in Lua.
--]]


-- When we run this program, it will output the following:
Name: John Doe
Age: 30

-- Note that since tuples are immutable, we cannot change the values in the person tuple once it has been created. However, we can create a new tuple with updated values if needed.