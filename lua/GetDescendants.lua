--[[
    In the Lua programming language, the GetDescendants() method is a function that is available on instances in the Roblox game engine.

    This function returns an array of all the descendants of the given instance. A descendant is any object that is a child of the instance or a child of a child of the instance, and so on.    
--]]

-- Get the Workspace object
local workspace = game:GetService("Workspace")

-- Get all the descendants of Workspace
local descendants = workspace:GetDescendants()

-- Print the name of each descendant
for _, descendant in ipairs(descendants) do
    print(descendant.Name)
end

--[[
    This code will print the name of every object in the Workspace hierarchy, including things like the Terrain, the Camera, and any models or parts that have been added to the game world.

    Note that the GetDescendants() method only works on instances, and not on other Lua types like tables or functions.    
--]]