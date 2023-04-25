--[[
    "PlayerRemoving" is a special event in Lua that is triggered when a player is about to be removed from the game. This event can be used to execute code or perform actions just before a player is removed, such as saving their progress or updating the game's data.

    To use the "PlayerRemoving" event, you first need to create a function that will handle the event. This function should take a single argument, which is the player that is being removed. Here's an example function:    
--]]

local function onPlayerRemoving(player)
    -- Code to execute when the player is about to be removed
    print("Player", player.Name, "is leaving the game")
end

-- Once you have your function, you can connect it to the "PlayerRemoving" event for each player you want to track. This can be done using the Connect() method of the player's Removing event, like this:

-- Get the first player in the game
local player = game:GetService("Players"):GetFirstChild()

-- Connect the function to the player's "Removing" event
player.Removing:Connect(onPlayerRemoving)

-- Now, whenever the player is about to be removed from the game, the onPlayerRemoving function will be called with the player as its argument. You can use this function to perform any actions you need to before the player is removed.


-- Example Program
-- Get the Players service
local Players = game:GetService("Players")

-- Function to save a player's progress
local function savePlayerProgress(player)
    print("Saving progress for player", player.Name)
    -- Code to save the player's progress
end

-- Function to handle the "PlayerRemoving" event
local function onPlayerRemoving(player)
    print("Player", player.Name, "is leaving the game")
    savePlayerProgress(player)
end

-- Connect the "PlayerRemoving" event for all players
Players.PlayerRemoving:Connect(onPlayerRemoving)

-- Print a message when the script has started
print("PlayerRemoving event connected")

/*
    In this program, we first get the Players service from the game. Then, we define a savePlayerProgress function that prints a message indicating that we are saving the player's progress (in this case, the function doesn't actually save anything, but you could replace this with your own code to save progress to a file or database).

    Next, we define an onPlayerRemoving function that prints a message indicating that a player is leaving the game, and then calls the savePlayerProgress function to save the player's progress.

    Finally, we connect the onPlayerRemoving function to the PlayerRemoving event for all players in the game using the Connect() method. When the script runs, it prints a message indicating that the PlayerRemoving event has been connected. Now, whenever a player leaves the game, the onPlayerRemoving function will be called to save their progress.
*/