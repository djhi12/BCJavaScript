
game.Players.PlayerAdded:connect(function(player) -- This line sets up a connection to the PlayerAdded event, which fires when a new player joins the game. The code inside the function will run every time a new player joins.
	player.CharacterAdded:connect(function(character) -- This line sets up a connection to the CharacterAdded event for the new player's character. The code inside the function will run every time the player's character is added to the game.

		if character:FindFirstChild("UpperTorso") then -- This line checks if the player's character has an UpperTorso object. If it does, the code inside the if block will run.

			script.RagdollClient:Clone().Parent = character -- This line creates a copy of the RagdollClient object in the script, and sets the parent of the copy to the player's character. This creates a ragdoll for the player's character.
			
			character:WaitForChild("Humanoid").Died:connect(function() -- This line sets up a connection to the Died event for the player's character's Humanoid object. The code inside the function will run when the character's Humanoid dies.

				character.UpperTorso:SetNetworkOwner(player) -- This line sets the network owner of the character's UpperTorso to the player. This is done so that when the player's character dies, the ragdoll will follow the player's movements instead of falling through the ground.

			end)
		end
	end)
end)

--[[
    Overall, this code creates a ragdoll for a player's character when they join the game, and sets up the necessary connections to ensure that the ragdoll behaves correctly when the player's character dies.    
--]]