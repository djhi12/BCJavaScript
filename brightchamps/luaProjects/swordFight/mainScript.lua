-- Define variables

local ReplicatedStorage = game:GetService("ReplicatedStorage") -- This line of code is retrieving the ReplicatedStorage service from the game and assigning it to the variable ReplicatedStorage. ReplicatedStorage is used to synchronize data between the server and the client in a Roblox game.

local ServerStorage = game:GetService("ServerStorage") -- This line of code is retrieving the ServerStorage service from the game and assigning it to the variable ServerStorage. ServerStorage is used to store game assets that are not needed by the client, such as server scripts and server-only game objects.

local MapsFolder = ServerStorage:WaitForChild("Maps") -- This line of code is retrieving a child object of the ServerStorage object called "Maps". It uses the WaitForChild method to ensure that the "Maps" object exists before assigning it to the variable MapsFolder. This object likely contains game assets related to the maps used in the game.

local Status = ReplicatedStorage:WaitForChild("Status") -- This line of code is retrieving a child object of the ReplicatedStorage object called "Status". It uses the WaitForChild method to ensure that the "Status" object exists before assigning it to the variable Status. This object likely contains data related to the game status that needs to be shared between the server and client.

local GameLength = 50 -- This line of code is assigning the value of 50 to the variable GameLength. This variable likely contains the length of the game in seconds.

local reward = 25 -- This line of code is assigning the value of 25 to the variable reward. This variable likely contains the amount of in-game currency or points a player will receive as a reward for completing a task or achieving a goal.

--Game Loop

while true do
	
	Status.Value = "Waiting for enough players" -- This line sets the Value property of a variable named Status to the string "Waiting for enough players".

	repeat wait(1) until game.Players.NumPlayers >= 2 -- This line starts a loop that waits 1 second (wait(1)) on each iteration until the number of players in the game (game.Players.NumPlayers) is greater than or equal to 2. In other words, the code will keep waiting until there are at least 2 players in the game. This is a common way to pause code execution until a certain condition is met.
	
	Status.Value = "Intermission" -- Once the loop in line 2 completes (because there are now at least 2 players), this line sets Status.Value to the string "Intermission".
    
	wait(10) -- This line pauses code execution for 10 seconds (wait(10)).Presumably, this is meant to simulate an intermission period between the waiting period and the start of the game.
	
	local plrs = {} -- This line creates a new empty table named plrs. Tables are Lua's primary data structure, and can be used to store arrays, key-value pairs, and other types of data.
	
	for i,player in pairs(game.Players:GetPlayers()) do -- This is a for loop that iterates through all of the players in the game. game.Players refers to a built-in object in the Roblox game engine that represents all of the players currently in the game. GetPlayers() is a method on this object that returns a list of all the players. The pairs() function is called on this list to get an iterator that iterates through all the players in the list. The for loop variable player is assigned to the current player in each iteration.

		if player then -- This line checks if the player variable is not nil. In other words, it checks if there is a player assigned to player in the current iteration of the loop.

			table.insert(plrs,player) -- If player is not nil, this line inserts the player object into a table called plrs. table.insert() is a built-in Lua function that adds an element to the end of a table. The plrs table is presumably defined elsewhere in the code.

		end -- This marks the end of the if statement.
	end -- This marks the end of the for loop.
	
	wait(2)
	
	local AvailableMaps = MapsFolder:GetChildren() -- This line declares a local variable AvailableMaps and assigns it the value returned by calling the GetChildren() method on the MapsFolder object. This method returns a table containing all of the immediate children of the MapsFolder object.
	
	local ChosenMap = AvailableMaps[math.random(1,#AvailableMaps)] -- This line declares a local variable ChosenMap and assigns it a randomly chosen element from the AvailableMaps table. The math.random() function is used to generate a random index between 1 and the length of the AvailableMaps table.
	
	Status.Value = ChosenMap.Name.."Chosen" -- This line sets the value of the Value property of the Status object to a string that includes the name of the ChosenMap object concatenated with the string "Chosen".

	local ClonedMap = ChosenMap:Clone() -- This line declares a local variable ClonedMap and assigns it a new instance of the ChosenMap object created by calling the Clone() method.

	ClonedMap.Parent = workspace -- This line sets the Parent property of the ClonedMap object to the workspace object, effectively moving the object into the game world.
	
	--Teleport players to the map
	
	local SpawnPoints = ClonedMap:FindFirstChild("SpawnPoints") -- This line declares a local variable SpawnPoints and assigns it the value returned by calling the FindFirstChild() method on the ClonedMap object. This method searches for a child object of the ClonedMap object with the name "SpawnPoints" and returns it if found, or nil if not found.
	
	if not SpawnPoints then -- this code checks if a variable called SpawnPoints exists and if it doesn't, it prints an error message to the console.
		print("SpawnPoints not found!")
	end
	
	local AvailableSpawnPoints = SpawnPoints:GetChildren() -- declares a local variable named AvailableSpawnPoints and assigns to it a list of all the children of the SpawnPoints object using the GetChildren() method. This code would typically be used in a Roblox game to get a list of available spawn points for players or objects.
	
	for i, player in pairs(plrs) do -- This line starts a loop that iterates through all elements of the plrs table using the pairs function. The i variable will hold the index of the current element, and player will hold the value of the current element.

		if player  then -- This line checks if the current element is not nil. If the current element is nil, the loop will skip to the next iteration.

			character = player.Character -- This line retrieves the Character object of the current player and assigns it to the character variable.
			
			if character then -- This line checks if the character variable is not nil. If the character variable is nil, the code in the else block will execute.

				character:FindFirstChild("HumanoidRootPart").CFrame = AvailableSpawnPoints[1].CFrame + Vector3.new(0,10,0) -- This line teleports the player's character to the first spawn point in the AvailableSpawnPoints table, adding a vertical offset of 10 units to avoid spawning inside the ground. The FindFirstChild function is used to retrieve the HumanoidRootPart object of the character, which is then used to set its CFrame property to the CFrame of the spawn point.

				table.remove(AvailableSpawnPoints,1) -- This line removes the first element of the AvailableSpawnPoints table, as it has just been used to teleport a player.
				
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
				end
			else
				table.remove(plrs,x)
				print(player.Name.." has been removed!")
			end
		end
		
		Status.Value = "There are "..i.." seconds remaining, and "..#plrs.."players left"
		
		if #plrs == 1 then
			--Last person standing
			Status.Value = "The winner is "..plrs[1].Name			
			plrs[1].leaderstats.Bucks.Value = plrs[1].leaderstats.Bucks.Value + reward
			break
		elseif #plrs == 0 then
			Status.Value = "Nobody won!"
			break
		elseif i==0 then		
			Status.Value = "Time up!"
			break
		end
		
		wait(1)
		
	end
	print("End of game")
	
	wait(2)
	
	for i, player in pairs(game.Players:GetPlayers()) do
		character = player.Character
		
		if not character then
			--Ignore them
		else
			if character:FindFirstChild("GameTag") then
				character.GameTag:Destroy()
			end
			
			if player.Backpack:FindFirstChild("Sword") then
				player.Backpack.Sword:Destroy()
			end
			
			if character:FindFirstChild("Sword") then
				character.Sword:Destroy()
			end
		end
		
		player:LoadCharacter()
	end
	
	ClonedMap:Destroy()
	
	Status.Value = "Game ended"
	wait(2)
end

