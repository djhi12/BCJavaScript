--[[
    In Lua, "nil" is a keyword that represents the absence of a value. It is used to indicate that a variable has not been assigned a value, or that a value has been explicitly removed.    
--]]

-- For example, if you define a variable like this:
local x

-- The value of x will be nil until you assign a value to it explicitly.


-- You can also use nil to remove a value from a variable, like this:
x = nil

-- This will set the value of x to nil, effectively removing any previously assigned value.


-- It's important to note that nil is a distinct value in Lua, and is not the same as a value that is empty or has a value of zero. It is also considered a false value in Lua's boolean logic.