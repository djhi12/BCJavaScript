--[[
    FindFirstChildOfClass is a function in Lua that searches for the first child of an instance that matches a specified class name. It is typically used in Roblox Lua programming to search for specific types of objects in a game's hierarchy.

    The function takes a single argument, which is a string representing the name of the class to search for. It returns the first child of the calling instance that matches the class name, or nil if no such child is found.    
--]]

-- Here's an example usage of the FindFirstChildOfClass function in Roblox Lua:
local player = game:GetService("Players"):FindFirstChild("Player1")
if player then
    local humanoid = player:FindFirstChildOfClass("Humanoid")
    if humanoid then
        -- do something with the humanoid object
    end
end

-- In this example, we're searching for a player object named "Player1" in the game's "Players" service. If the player object is found, we use FindFirstChildOfClass to search for a "Humanoid" object among its children. If a humanoid object is found, we can then manipulate it in some way.