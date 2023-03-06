--[[
    In Lua, the colon symbol (":") is used as a syntactic sugar to simplify method calls that involve passing the object instance as the first parameter.    
--]] -- When you define a method in Lua, you typically write it using the dot notation, like this:

function obj:method(param1, param2, ...)
    -- method implementation
end

-- In this case, obj is an instance of some class or table, and method is a function that takes two or more parameters. The colon notation is simply a shorthand for this:

function obj.method(self, param1, param2, ...)
    -- method implementation
end

-- Using the colon notation allows you to call the method on an instance of the class or table, like this:
obj:method(param1, param2, ...)


-- In this case, Lua automatically passes the instance obj as the first parameter to the method. If you were to use the dot notation, you would have to explicitly pass the instance as the first parameter, like this:
obj.method(obj, param1, param2, ...)

--[[
    So, the colon notation makes code more concise and easier to read.    
--]]
