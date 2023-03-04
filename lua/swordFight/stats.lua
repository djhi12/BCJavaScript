local dataStores = game:GetService("DataStoreService"):GetDataStore("BucksDataStore")
local defaultCash = 10
local playersLeft = 0

game.Players.PlayerAdded:Connect(function(player)
	
	--playersLeft = playersLeft + 1
	
	--to  create a leaderboard
	local leaderstats = Instance.new("Folder")
	leaderstats.Name = "leaderstats"--leaderstats should be mentioned like this only, otherwise the leaderboard will not pop up
	
	--parent the leaderstats folder so that every player will have their own folder called leaderstats
	leaderstats.Parent = player
	
	--create a variable for the currency
	local bucks = Instance.new("IntValue") --IntValue means integer value since currency will be in the form of numbers
	bucks.Name = "Bucks"
	bucks.Value = 0 							--Initally the value will be 0
	bucks.Parent = leaderstats
	
	player.CharacterAdded:Connect(function(character)
		character.Humanoid.WalkSpeed = 16
		character.Humanoid.Died:Connect(function()
			--whenever somebody dies, this event will run
			
			if character.Humanoid and character.Humanoid:FindFirstChild("creator") then
				game.ReplicatedStorage.Status.Value = tostring(character.Humanoid.creator.Value).." KILLED "..player.Name
			end
			
			
			if character:FindFirstChild("GameTag") then
				character.GameTag:Destroy()
			end
			player:LoadCharacter()
		end)
	end)
	
	--Data Stores
	
	local player_data
	
	pcall (function()
		player_data = dataStores:GetAsync(player.UserId.." -Bucks")
	end)
	
	if player_data ~= nil then
		--player has saved data, load it in
		bucks.Value = player_data
	else
		--New Player
		bucks.Value = defaultCash
	end
	
end)

local bindableEvent = Instance.new("BindableEvent")

game.Players.PlayerRemoving:Connect(function(player)
	pcall(function()
		dataStores:SetAsync(player.UserId.."-Bucks",player.leaderstats.Bucks.Value)
		print("Saved") 
		playersLeft = playersLeft-1
		bindableEvent:Fire()
	end)
end)


game:BindToClose(function()
	--This will be triggered upon shutdown
	while playersLeft > 0 do
		bindableEvent.Event:Wait()
	end
end)