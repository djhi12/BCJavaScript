local Round = require(script.RoundModule)
local Door = require(script.DoorModule)

local status = game.ReplicatedStorage:WaitForChild("Status")

repeat 
	local availableplrs = {}
	for i, plr in pairs(game.Players:GetPlayers()) do
		if not plr:FindFirstChild("InMenu") then
			table.insert(availableplrs,plr)
		end
		--when the player click the play button so they will be listed on the available players
	end
	
	status.Value = "2 'Ready' players needed ("..#availableplrs.."/2)"
	
	wait(2)
	--this loop will check every 2 seconds, so it won't check everytime--
	
until #availableplrs >=2
--when available players needed already fulfilled, then it will break this loop
--then the intermission starts


while wait() do
	Round.Intermission(5)

	local chosenChapt = Round.SelectChapter()

	local clonedChapt = chosenChapt:Clone()
	--to copy the map from the ReplicatedStorage--
	clonedChapt.Name = "Map"
	clonedChapt.Parent = game.Workspace
	--set the map on the workspace so we can see it--
	
	wait(3)
	
	if clonedChapt:FindFirstChild("Doors") then
		Door.ActivateDoors(clonedChapt.Doors)
	else
		warn("ERROR: You didn't add the Doors folder on your map")
	end

	local contestants = {}
	for i, v in pairs(game.Players:GetPlayers()) do
		if not v:FindFirstChild("InMenu") then
			--so if the player already click the "Play" button, it will be listed as contestant--
			table.insert(contestants,v)
			print("Added player "..v.Name.." to contestants")
		end
	end

	local chosenPiggy = Round.SelectPiggy(contestants)

	for i, v in pairs(contestants) do
		if v == chosenPiggy then
			table.remove(contestants,i)			
		end
	end
	
	for i, v in pairs(contestants) do
		if v~= chosenPiggy then
			game.ReplicatedStorage.ToggleCrouch:FireClient(v,true)		
		end
	end
	--so if it is not a piggy, the togglecrouch will appear
	
	wait(2)

	Round.DressPiggy(chosenPiggy)

	Round.TeleportPiggy(chosenPiggy)


	if clonedChapt:FindFirstChild("PlayerSpawns") then
		Round.TeleportPlayers(contestants, clonedChapt.PlayerSpawns:GetChildren())
	else
		warn("ERROR: You didn't add a PlayerSpawns Folder on your map")	
	end
	--just to make sure the playerspawns there--


	Round.InsertTag(contestants, "Contestant")
	Round.InsertTag({chosenPiggy}, "Piggy")
	--every player will have a stringvalue as the tag
	--for contestant it will be named "Contestant", for piggy it is named "Piggy"
	
	print("tag")
	print("timer starts")
	
	Round.StartingRound(600, chosenPiggy, clonedChapt)

	print("end")

	contestants = {}

	for i, v in pairs(game.Players:GetPlayers()) do
		if not v:FindFirstChild("InMenu") then
			table.insert(contestants,v)
		end
	end

	if game.Workspace.Lobby:FindFirstChild("Spawns") then
		Round.TeleportPlayers(contestants, game.Workspace.Lobby.Spawns:GetChildren())
	else
		warn("ERROR: You didn't add a Spawns Folder into your Lobby")	
	end

	clonedChapt:Destroy()

	Round.RemoveTags()
	
	wait(2)
end