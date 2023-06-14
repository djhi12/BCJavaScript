--[[
    In Lua, a "vector" can be represented as a table with two or three numeric components, depending on whether it's a two-dimensional or three-dimensional vector. Here's an example of a two-dimensional vector table:    
--]]

local vec2 = { x = 2, y = 5 }


-- And here's an example of a three-dimensional vector table:
local vec3 = { x = 1, y = 3, z = 2 }


-- You can perform operations on vectors by accessing their components and applying mathematical functions to them. For example, you can add two vectors together by adding their corresponding components:
local vec1 = { x = 1, y = 2 }
local vec2 = { x = 3, y = 4 }
local result = { x = vec1.x + vec2.x, y = vec1.y + vec2.y }
print(result.x, result.y) -- Output: 4    6


-- Alternatively, you can define a function to perform vector addition:
function addVectors(vec1, vec2)
    return { x = vec1.x + vec2.x, y = vec1.y + vec2.y }
end
  
local vec1 = { x = 1, y = 2 }
local vec2 = { x = 3, y = 4 }
local result = addVectors(vec1, vec2)
print(result.x, result.y) -- Output: 4    6

  
-- You can also perform dot products and cross products on vectors, as well as other operations. Lua doesn't have built-in support for vector operations, but you can define your own functions or use a library like LuaMath to handle them.