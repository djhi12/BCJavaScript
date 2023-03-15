-- Define variables

local ReplicatedStorage = game:GetService("ReplicatedStorage") 

local ServerStorage = game:GetService("ServerStorage")

local MapsFolder = ServerStorage:WaitForChild("Maps")

local Status = ReplicatedStorage:WaitForChild("Status")

local GameLength = 50
local reward = 25

--Game Loop

while true do
	
	Status.Value = "Waiting for enough players"
	repeat wait(1) until game.Players.NumPlayers >= 2
	
	Status.Value = "Intermission"
	wait(10)
	
	local plrs = {}
	
	for i,player in pairs(game.Players:GetPlayers()) do
		if player then
			table.insert(plrs,player) --add each player into plrs table
		end
	end
	
	wait(2)
	
	local AvailableMaps = MapsFolder:GetChildren()
	
	local ChosenMap = AvailableMaps[math.random(1,#AvailableMaps)]
	
	Status.Value = ChosenMap.Name.."Chosen"
	local ClonedMap = ChosenMap:Clone()
	ClonedMap.Parent = workspace
	
	--Teleport players to the map
	
	local SpawnPoints = ClonedMap:FindFirstChild("SpawnPoints")
	
	if not SpawnPoints then
		print("SpawnPoints not found!")
	end
	
	local AvailableSpawnPoints = SpawnPoints:GetChildren()
	
	for i, player in pairs(plrs) do
		if player  then
			character = player.Character
			
			if character then
				--Teleport them
				character:FindFirstChild("HumanoidRootPart").CFrame = AvailableSpawnPoints[1].CFrame + Vector3.new(0,10,0)
				table.remove(AvailableSpawnPoints,1)
				
				--Give player a sword
				local Sword = ServerStorage.Sword:Clone()
				Sword.Parent = player.Backpack
				
				local GameTag = Instance.new("BoolValue")
				GameTag.Name = "GameTag"
				GameTag.Parent = player.Character
				
				
				
			else
				--There is no character
				if not player then
					table.remove(plrs,i)
				end 
			end
		end
	end
	
	Status.Value = "Get Ready to play!"
	wait(2)
	
	for i = GameLength,0,-1 do
		 
		for x, player in pairs(plrs) do		
			
			if player then
				character = player.Character
				if not character then
					--Left the game
					table.remove(plrs,x)
				else
					if character:FindFirstChild("GameTag") then
						--They are still alive
						print(player.Name.." is still in the game!")
					else
						--They are Dead
						table.remove(plrs,x)
						print(player.Name.." has been removed!")
					end