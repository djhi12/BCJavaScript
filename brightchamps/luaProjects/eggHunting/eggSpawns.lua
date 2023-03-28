local eggs = game.ReplicatedStorage.Eggs --variable for the eggs in replicated storage

local spawns = game.Workspace.EggSpawns --variable for spawns in spawns folder

while wait(2) do --to select the random egg and spawn every 2 seconds to put it out in the location
	--anything inside this while loop will keep on running for every two seconds
	
	--create a table for all of the eggs that are present in the folder
	local eggsTable = eggs:GetChildren() --This will help in getting all of the eggs in the folder
	
	--random egg pick out of the table
	local randomEgg = eggsTable[math.random(1,#eggsTable)] --value for random will be 1 and however items are their in the table, #eggstable will give the amount of items in that table
	
	--create a table to choose the random spawn
	local spawnsTable = spawns:GetChildren()
	
	--to pick a random spawn from the table
	local randomSpawn = spawnsTable[math.random(1,#spawnsTable)]
	
	--After getting a random egg, create a clone of it to not use the egg which is their in replicated storage
	
	local eggClone = randomEgg:Clone()
	
	--to put the cloned egg in a new folder
	eggClone.Parent = game.Workspace.SpawnedEggs
	
	--to set the position of the cloned egg
	eggClone.Position = randomSpawn.Position + Vector3.new(0,20,0) --to get the current position of the random spawn and moving it to 20 studs y axis
	eggClone.Anchored = false
	
	--touch event when the egg has been touched by the player
	eggClone.Touched:Connect(function(hit) --hit is the arguement, an object which touches the egg
		--when the egg has been touched, delete it but also make the GUI appear
		
		--to check whether egg has been touched by the player or not
		local playr = game.Players:GetPlayerFromCharacter(hit.Parent) --this will return true or false, depending egg got hit by the players body only
		
		if playr then
			--if true, make the GUI appear on the screen
			game.ReplicatedStorage.FoundEgg:FireClient(playr,eggClone.Name) --with fireclient we are sending a request to a certain player to do something on their end
			eggClone:Destroy()
		end
		
	end)
	
end