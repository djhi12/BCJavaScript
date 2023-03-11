local dataStores = game:GetService("DataStoreService"):GetDataStore("BucksDataStore") -- The first line of code creates a variable called "dataStores" and assigns it the value of the DataStoreService's GetDataStore method called "BucksDataStore". This method is used to get a DataStore object with the name "BucksDataStore". The DataStoreService is a Roblox service that allows games to store and retrieve data for players across sessions.

local defaultCash = 10 -- The second line of code creates a variable called "defaultCash" and assigns it the value of 10. This is likely a default value for the amount of currency a player has if they have not yet earned any in the game.

local playersLeft = 0 -- The third line of code creates a variable called "playersLeft" and assigns it the value of 0. This variable might be used to keep track of how many players are still active in the game.

game.Players.PlayerAdded:Connect(function(player) -- game.Players refers to a table that holds all the players currently in the game. The PlayerAdded event is fired by Roblox when a new player joins the game. The :Connect() method is used to register a function to be called when this event is fired.

    --[[ 
        In this case, the function passed to :Connect() takes one argument, player, which represents the player who just joined the game. The code inside the function will be executed every time a new player joins the game.    
    --]]
	
	playersLeft = playersLeft + 1 -- This Lua code increases the value of a variable named "playersLeft" by 1.
	

	local leaderstats = Instance.new("Folder") -- This Lua code creates a new folder object called leaderstats and sets its name to "leaderstats" using the Instance.new() function. The Instance.new() function creates a new instance of a Roblox object, in this case, a folder.

	leaderstats.Name = "leaderstats"
	leaderstats.Parent = player -- The code then sets the parent of the leaderstats folder to a player object. This means that the leaderstats folder will be a child of the player object in the hierarchy of the Roblox game.

    --[[  
        This code is often used in games to create a place to store player-specific data such as a player's score or game progression. By creating a leaderstats folder and attaching it to the player object, the game can keep track of each player's progress separately.    
    --]]
	

	local bucks = Instance.new("IntValue") -- This code creates a new IntValue object called bucks using the Instance.new() function. The IntValue class is used to represent an integer value in Lua.

	bucks.Name = "Bucks" -- Next, the code sets the Name property of bucks to "Bucks".This sets the name of the IntValue object to "Bucks".

	bucks.Value = 0 -- Then, the code sets the Value property of bucks to 0.

	bucks.Parent = leaderstats -- This sets the parent of the bucks object to leaderstats, which is presumably another object in the script.
	
	player.CharacterAdded:Connect(function(character) -- In Roblox, Player objects represent the players in a game. Each Player object has a Character object that represents the player's in-game avatar. The CharacterAdded event is fired when a player's character is added to the game.

		character.Humanoid.WalkSpeed = 16 --this code is setting the walk speed of the specified character to 16 units per second.

		character.Humanoid.Died:Connect(function()
			--whenever somebody dies, this event will run
			
			if character.Humanoid and character.Humanoid:FindFirstChild("creator") then
				game.ReplicatedStorage.Status.Value = tostring(character.Humanoid.creator.Value).." KILLED "..player.Name
			end -- This Lua code checks if the variable "character" has a child object named "Humanoid" and if that object also has a child object named "creator". If both conditions are met, then it sets the value of a "Status" value in the "ReplicatedStorage" object to a string that includes the value of the "creator" object concatenated with "KILLED" and the name of a player.
			
			
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