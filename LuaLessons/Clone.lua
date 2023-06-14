--[[
    In Lua, the ":Clone()" method is not a built-in function, but it can be used in the context of an object-oriented programming (OOP) framework to create a copy of an object. The ":Clone()" method is typically defined in a class or metatable as a member function.

    When called on an object, the ":Clone()" method returns a new copy of the object with the same values for all its properties. The newly created object is independent of the original object and any changes made to one will not affect the other.    
--]] 


-- Here is an example of how ":Clone()" could be implemented in a simple OOP framework in Lua:
-- define a class
Person = {name = "", age = 0}

-- define a "Clone" method for the class
function Person:Clone()
    local clone = {}
    for k, v in pairs(self) do clone[k] = v end
    return setmetatable(clone, getmetatable(self))
end

-- create an instance of the class
local john = setmetatable({name = "John", age = 30}, {__index = Person})

-- clone the instance
local john_clone = john:Clone()

-- print the values of the original and cloned objects
print(john.name, john.age) -- prints "John 30"
print(john_clone.name, john_clone.age) -- prints "John 30"

-- modify the original object
john.name = "John Doe"
john.age = 35

-- print the values of the original and cloned objects again
print(john.name, john.age) -- prints "John Doe 35"
print(john_clone.name, john_clone.age) -- prints "John 30"


--[[
    In this example, the "Person" class is defined with two properties: "name" and "age". The ":Clone()" method is defined to create a new table and copy all the properties of the object into the new table. The "__index" metamethod is used to allow the object to inherit from the "Person" class.

    A new instance of the "Person" class is created and stored in the "john" variable. The ":Clone()" method is then called on the "john" object to create a new copy of it, which is stored in the "john_clone" variable. The values of the "name" and "age" properties of both the original and cloned objects are printed.

    The original "john" object is then modified by changing the values of its "name" and "age" properties. The values of the "name" and "age" properties of both the original and cloned objects are printed again to show that the cloned object was not affected by the changes made to the original object.    
--]]