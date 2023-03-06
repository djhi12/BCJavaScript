local module = {}

local status = game.ReplicatedStorage:WaitForChild("Status")


function module.Intermission(length)
	--length means how many seconds the count down, 0 means it will keep counting down until 0, -1 means the second will be decreased by 1--
	for i = length,0,-1 do
		status.Value = "Next round starts in "..i.." seconds"
		--status.Value is the value that will be displayed on the screen--
		--".." uses to combine all the text--
		wait(1)
		--it will change the status every 1 second--
	end
end

function module.SelectChapter()
	local rand = Random.new()
	local chapters = game.ReplicatedStorage.Chapters:GetChildren()
	--get children is the table of chapter maps in the chapters folder--
	local chosenChapt = chapters[rand:NextInteger(1,#chapters)]
	--#chapters is the length of chapters table--
	
	return chosenChapt
	--returning the chosenmap--
end

function module.SelectPiggy(players)
	local randm = Random.new()
	local chosenPiggy = players[randm:NextInteger(1,#players)]
	--#players is the length of players table--
	-- this will select random player to become the piggy--

	return chosenPiggy
	--returning the chosenpiggy--
end

function module.DressPiggy(piggy)
	local piggycharacter = game.ServerStorage.Piggy:Clone()
	piggycharacter.Name = piggy.Name
	piggy.Character = piggycharacter
	piggycharacter.Parent = game.Workspace
end

function module.TeleportPiggy(piggyplayer)
	if piggyplayer.Character then
		piggyplayer.Character.Humanoid.WalkSpeed = 14
		--the default walkspeed is 16, so piggy will walk slower--
		
		local piggybatclone = game.ServerStorage.Tools.PiggyBat:Clone()
		piggybatclone.Parent = piggyplayer.Character
		--so the bat will be equiped by piggy--
		
		if piggyplayer.Character:FindFirstChild("HumanoidRootPart") then
			piggyplayer.Character.HumanoidRootPart.CFrame = game.Workspace.WaitingRoom.PiggyWaitingSpawn.CFrame + Vector3.new(0,5,0)
			--piggy will be teleported to piggyspawn in waiting room--
			--y position of piggy is over than the spawner because it will make him spawn on top of the spawner)
		end
		
		local trapcount = Instance.new("IntValue")
		trapcount.Name = "TrapCount"
		trapcount.Value = 5
		trapcount.Parent = piggyplayer
		
		game.ReplicatedStorage.ToggleTrap:FireClient(piggyplayer,true)
		--so the trapgui only appear on piggy screen
		
		
	end
end

function module.TeleportPlayers(players, mapSpawns)
	for i, player in pairs(players) do
		if player.Character then
			if player.Character:FindFirstChild("HumanoidRootPart") then
				--just to make sure the character there--

				local char = player.Character
				
				player.Character.Humanoid.WalkSpeed = 16
				--set the speed of players to default speed or you can make them faster--
				
				local randm = Random.new()
				player.Character.HumanoidRootPart.CFrame = mapSpawns[randm:NextInteger(1,#mapSpawns)].CFrame + Vector3.new(0,5,0)
				--set the players on the top of spawn--
				
				local hitboxclone = game.ServerStorage.Hitbox:Clone()
				hitboxclone.CFrame = char.HumanoidRootPart.CFrame
				--this will set the position of the hitbox is at player position
				
				local weld = Instance.new("Weld")
				weld.Part1 = char.HumanoidRootPart
				weld.Part0 = hitboxclone
				weld.Parent = hitboxclone
				--this will join hitbox to player character
				
				hitboxclone.Parent = char
				print(hitboxclone.Parent)
			end
		end
	end	
end

function module.InsertTag(players, tagName)
	for i, player in pairs(players) do
		local tag = Instance.new("StringValue")
		tag.Name = tagName
		tag.Parent = player
		print(tagName)
	end
end

local function convertSecToMin(s)
	return ("%02i:%02i"):format(s/60%60, s%60)
	--this will convert 600 seconds to 10:00--
end

function module.StartingRound(length, piggy, chapterMap)
	local info
	
	game.ServerStorage.GameValues.GameInProgress.Value = true
	
	
	--length in second--	
	for i = length,0,-1 do
		--length is the duration of the round--
		--0 is the time when timer stops--
		-- -1 means it will count down--
		
		local escapees = 0
		--number of player that could open the "ExitDoor"
		
		if i==(length-20)then
			module.TeleportPlayers({piggy}, chapterMap.PlayerSpawns:GetChildren())
			--this will teleport piggy to the map after 20 secs
			--we don't use TeleportPiggy function because that only teleport piggy to piggy waiting room
			
			status.Value = "Piggy has woken up!"
			wait(2)
			--there will be 2 secs delay after piggy been released to the map--
		end
		
		local contestants = {}
		local ispiggyhere = false
		--contestants table will store all players that still survive
		--ispiggyhere will check is the piggy left or still in the game
		
		
		for i, player in pairs(game.Players:GetPlayers()) do
			if player:FindFirstChild("Contestant") then
				table.insert(contestants,player)
			elseif player:FindFirstChild("Piggy") then
				ispiggyhere = true
			end
			
			if player:FindFirstChild("Escaped") then
				escapees +=1
			end
			--when
			
		end
		
		if not ispiggyhere then
			info = "piggy left"
			break
		end
		--this will inform that no piggy anymore, then stop the loop
		
		
		if #contestants == 0 then
			info = "no more contestants"
			break
		end
		--this will inform that no contestants anymore, then stop the loop
		
		if i == 0 then
			info = "time up"
			break
		end
		--this will inform that time is up, then stop the loop
		
		
		status.Value = convertSecToMin(i)
		wait(1)
	end
	
	if info == "no more contestants" then
		status.Value = "The Piggy Has Killed Everyone, Piggy Wins!"
	end
	
	if info == "time up" then
		status.Value = "Time Up! Contestants Win!"
	end
	
	if info == "piggy left" then
		status.Value = "Piggy has died / left! Contestants Win!"
		print("a")
	end
	print(info)
	wait(5)
	--so the message can be read for some seconds
end

function module.RemoveTags()
	
	game.ServerStorage.GameValues.GameInProgress.Value = false
	
	game.ReplicatedStorage.ToggleCrouch:FireAllClients()
	
	for i,v in pairs(game.Players:GetPlayers()) do
		if v:FindFirstChild("Piggy") then
			v.Piggy:Destroy()
			
			if v.Backpack:FindFirstChild("PiggyBat") then v.Backpack.PiggyBat:Destroy() end
			if v.Character:FindFirstChild("PiggyBat") then v.Character.PiggyBat:Destroy() end
			--so piggy will not equip/bring the piggybat when the game is over
			
			if v:FindFirstChild("TrapCount") then
				v.TrapCount:Destroy()
			end
			--so after the round end, the trapcount value dissapear
			
			game.ReplicatedStorage.ToggleTrap:FireClient(v,false)
			--trap gui disable when the round end
			
			
			v:LoadCharacter()
			--so this will undress the piggy
			
		elseif v:FindFirstChild("Contestant") then
			v.Contestant:Destroy()
			
			for j,p in pairs(v.Backpack:GetChildren()) do
				if p:IsA("Tool") then p:Destroy() end
			end
			
			for j,p in pairs(v.Character:GetChildren()) do
				if p:IsA("Tool") then p:Destroy() end
			end
			--this will delete the tool on contestant
			-- j and p just different variable name because it is for loop inside a for loop, just choose different name
			
		end
	end
	
end


return module
