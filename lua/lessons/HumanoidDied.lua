--[[
    "Humanoid.Died" in Lua is an event that fires when a Roblox character's humanoid dies. It is commonly used in Roblox game development to detect when a player or NPC's health reaches zero and they die in the game.

    The "Humanoid" object in Roblox represents a character's body, and it has a "Died" event that is triggered when the character's health drops to zero. Developers can use this event to perform actions such as respawning the character, displaying a message, or updating a score.    
--]]

local player = game.Players.LocalPlayer
local character = player.Character or player.CharacterAdded:Wait()

local humanoid = character:WaitForChild("Humanoid")
humanoid.Died:Connect(function()
   -- code to run when the character dies
   print("You died!")
end)


--[[
    In this example, we are getting the local player's character and connecting the "Died" event of its humanoid. When the character dies, the code inside the function will be executed, which in this case will simply print "You died!" to the console.    
--]]