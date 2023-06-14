--[[
    In Lua, the ":Create()" syntax is typically used as a convention to define a class constructor or factory method.

    When a method is defined using the ":" operator instead of the "." operator, it automatically takes an implicit first parameter (conventionally named self) that refers to the object on which the method is being called.

    Therefore, calling obj:Create() on an object obj of a class that defines a Create method using the ":" syntax would invoke the Create method with obj as the implicit self parameter.    
--]]

-- Here's an example of a simple class definition using this syntax:
-- define a simple class
local MyClass = {}

function MyClass:Create(x, y)
  local obj = {}
  obj.x = x
  obj.y = y
  setmetatable(obj, self)
  self.__index = self
  return obj
end

-- create an instance of the class
local myObj = MyClass:Create(10, 20)

-- access the instance variables
print(myObj.x) --> 10
print(myObj.y) --> 20

-- In this example, MyClass:Create(x, y) is defined as the class constructor method that takes two parameters x and y, and returns a new object with x and y as its instance variables. The setmetatable and __index lines are used to set up inheritance for the class. Finally, myObj is created by calling MyClass:Create(10, 20) with the appropriate arguments.