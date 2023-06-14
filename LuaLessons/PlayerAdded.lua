--[[
    "PlayerAdded" is an event in the Lua programming language that is fired whenever a new player joins the game. It is often used in games or other interactive applications where new players need to be identified and handled differently than existing players.

    To use the "PlayerAdded" event in Lua, you can first get a reference to the game's "Players" service, which contains information about all of the players currently in the game. You can then connect a function to the "PlayerAdded" event using the "Connect" method, like this:    
--]]

game.Players.PlayerAdded:Connect(function(player)
    -- Code to run when a new player joins the game
end)

-- Inside the function, you can perform any actions you need to when a new player joins the game, such as setting up their character, displaying a welcome message, or assigning them to a team. The "player" parameter passed to the function will be a reference to the new player that just joined.