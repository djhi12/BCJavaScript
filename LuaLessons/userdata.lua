--[[
    In Lua, "userdata" is a type of value that represents an arbitrary block of memory. This type of value is often used to interface with C or other programming languages, as it allows Lua code to access and manipulate data that is stored outside of the Lua runtime environment.

    Userdata values are created using the lua_newuserdata function, which allocates a block of memory of a specified size and associates it with a Lua value. Once a userdata value has been created, it can be manipulated using a variety of functions provided by the Lua API.

    For example, suppose you have a C library that provides a function for computing the dot product of two vectors, and you want to expose this functionality to Lua code. You could create a userdata value to represent each vector, and then provide a Lua function that calls the C library's dot product function using the userdata values.    
--]]

-- Lua code
-- create two userdata values to represent vectors
local a = ffi.new("Vector3")
a.x = 1
a.y = 2
a.z = 3

local b = ffi.new("Vector3")
b.x = 4
b.y = 5
b.z = 6

-- define a Lua function to compute the dot product using the userdata values
local function dot_product(a, b)
  return ffi.C.dot_product(a, b)
end

-- call the dot product function with the userdata values
print(dot_product(a, b)) --> 32

-- In this example, the ffi.new function is used to create two userdata values, a and b, that represent two 3D vectors. The dot_product function is defined in Lua to call the C library's dot_product function using the userdata values. Finally, the dot product is computed by calling the dot_product function with the two userdata values as arguments.