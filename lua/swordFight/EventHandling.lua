local keymod = require(script.Parent:WaitForChild("Game Logic").KeyModule)
local roundmod = require(script.Parent:WaitForChild("Game Logic").RoundModule)

game.Players.PlayerAdded:Connect(function(player)
	--PlayerAdded is an event, whenever player started to join the game, this function will run--
	local inMenu = Instance.new("BoolValue")
	inMenu.Name = "InMenu"
	inMenu.Parent = player
	--this boolvalue will appear in each player"
	
	player.CharacterAdded:Connect(function(char)
		char.Humanoid.Died:Connect(function()
			if char:FindFirstChild("HumanoidRootPart") then
				keymod.DropTool(player,game.Workspace.Map,char.HumanoidRootPart.Position)
				print("tools are dropped")
			end
			
			if player:FindFirstChild("Piggy") then
				player.Piggy:Destroy()
				--when the piggy dies, the piggy tag will be destroyed
			end
			
			if player:FindFirstChild("Contestant") then
				player.Contestant:Destroy()
				--when the player dies, the contestant tag will be destroyed
			end		
		end)
	end)
	
end)


local trapdebounce = false

game.ReplicatedStorage.PlaceTrap.OnServerEvent:Connect(function(player)
	if player:FindFirstChild("Piggy") then
		--so only piggy who able to place the trap
		
		if player:FindFirstChild("TrapCount") then
			if not trapdebounce then
				trapdebounce = true
				
				if player.TrapCount.Value > 0 then
					if game.Workspace:FindFirstChild("Map") then
						player.TrapCount.Value -= 1
						--this will decrease the trapcount by 1
						
						local trapclone = game.ServerStorage.Bear_Trap:Clone()
						trapclone.CFrame = player.Character.HumanoidRootPart.CFrame - Vector3.new(0, 3.5, 0)
						--the position of the trap will be at bottom of the player
						
						trapclone.Parent = game.Workspace:FindFirstChild("Map")
						
					end
				end
				
				wait(5)
				trapdebounce = false
			end
		end
	end
end)

game.ReplicatedStorage.MenuPlay.OnServerEvent:Connect(function(player)
	if player:FindFirstChild("InMenu") then
		player.InMenu:Destroy()
	end
	
	if game.ServerStorage.GameValues.GameInProgress.Value == true then
		local contestantTag = Instance.new("BoolValue")
		contestantTag.Name = "Contestant"
		contestantTag.Parent = player
		
		game.ReplicatedStorage.ToggleCrouch:FireClient(player,true)
		
		roundmod.TeleportPlayers({player}, game.Workspace:FindFirstChild("Map").PlayerSpawns:GetChildren())
		--new player will be teleported to map immediately
	end
end)
