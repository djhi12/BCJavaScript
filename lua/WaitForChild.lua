--[[
    "WaitForChild" is a method in Lua that is commonly used in Roblox Lua programming. It is a function that waits for a specific child object of a parent object to exist before continuing with the code execution.

    In Roblox Lua, game objects (such as parts, models, and scripts) are organized into a hierarchy of parent-child relationships. The WaitForChild method is typically used to find a specific child object of a parent object.    
--]]


-- The syntax of the WaitForChild method is as follows:
local child = parent:WaitForChild(childName)

--[[
    This code will wait until a child object with the name "childName" exists as a child of the "parent" object. Once the child object is found, it is returned and assigned to the "child" variable.

    If the child object does not exist within a certain timeout period (which defaults to 5 seconds), then the method will throw an error.

    Overall, the WaitForChild method is a useful tool in Roblox Lua programming for ensuring that code execution does not proceed until the necessary objects are available.
--]]


-- Example Code
-- Get the player's character
local player = game.Players.LocalPlayer
local character = player.Character or player.CharacterAdded:Wait()

-- Get the humanoid root part
local humanoidRootPart = character:WaitForChild("HumanoidRootPart")

-- Move the humanoid root part
humanoidRootPart.CFrame = CFrame.new(0, 10, 0)

--[[
    In this code, we first retrieve the player's character object using the "LocalPlayer" property. We then use the "WaitForChild" method to find the "HumanoidRootPart" object of the character. Once we have the "HumanoidRootPart" object, we can manipulate it by setting its CFrame property to move the character's position.

    Note that we use the "or" operator and the "Wait" method to handle the case where the character object is not immediately available. If the "Character" property is nil, we wait for the "CharacterAdded" event to fire before continuing. This ensures that we don't try to access the "HumanoidRootPart" object before the character object is fully initialized.
--]]


