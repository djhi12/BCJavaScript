local TweenService = game:GetService("TweenService")
local Players = game:GetService("Players")
local ReplicatedStorage = game:GetService("ReplicatedStorage")

local Map = game.Workspace.Map
local Doll = Map.Doll
local TimerUI = Map.Timer.UI

local ROUND_DURATION_SECONDS = 60 --1 minute

local isRedLight = ReplicatedStorage.isRedLight
local savedPlayerPositions = {} --logging all player positions when there is a red light, so we can later check their movements
local SpinTweenInfo = TweenInfo.new(1, Enum.EasingStyle.Linear, Enum.EasingDirection.InOut)

local OriginalHeadCFrame = Doll.Head.CFrame

local GreenLightHead = TweenService:Create(Doll.Head, SpinTweenInfo, {
	CFrame = OriginalHeadCFrame
})

local RedLightHead = TweenService:Create(Doll.Head, SpinTweenInfo, {
	CFrame = OriginalHeadCFrame * CFrame.Angles(0,math.rad(180),0) --180 Degrees Rotation
})

function DressCharacterInSuit(character)
	for _, object in pairs(character:GetChildren()) do
		if object:IsA("Shirt") or object:IsA("Pants") or object:IsA("ShirtGraphic") then
			object:Destroy()
		end
	end
	
	local Shirt = Instance.new("Shirt")
	Shirt.ShirtTemplate = "rbxassetid://7597521537"
	Shirt.Parent = character
	
	local Pants = Instance.new("Pants")
	Pants.PantsTemplate = "rbxassetid://7597288954"
	Pants.Parent = character
	
end

function SecondsToTimestamp(seconds)
	seconds = math.max(seconds, 0)
	
	local minutes = tostring(math.floor(seconds/60))
	local leftoverSeconds = tostring(seconds%60)
	
	if #leftoverSeconds ==1 then
		leftoverSeconds = "0"..leftoverSeconds
	end
	return tostring(minutes)..":"..leftoverSeconds
end

function LogPlayerPositions(players)
	for _, player in pairs(players) do
		if player.Character then
			local HumanoidRootPart = player.Character:FindFirstChild("HumanoidRootPart")
			if HumanoidRootPart then
				savedPlayerPositions[player] = HumanoidRootPart.Position
			end
		end
	end
end

function StartGame()
	
	GreenLightHead:Play()
	isRedLight.Value = false
	savedPlayerPositions = {}
	
	local playersInRound = Players:GetPlayers()
	local winners = {}
	local spinDelay = 3
	local lastSpin = tick()
	local endTouch
	
	for _, player in pairs(playersInRound) do
		player:LoadCharacter()
		DressCharacterInSuit(player.Character)
	end
	
	endTouch = Map.EndBarrier.Touched:Connect(function(toucher)
		if not toucher or not toucher.Parent then
			return
		end
		
		local touchChar = toucher.Parent
		local touchPlayer = Players:GetPlayerFromCharacter(touchChar)
		
		if touchPlayer then
			local winnersIndex = table.find(winners, touchPlayer)
			if winnersIndex then return end
			
			table.insert(winners, touchPlayer)
			local playerIndex = table.find(playersInRound, touchPlayer)
			if playerIndex then
				table.remove(playersInRound, playerIndex)
			end
		end	
	end)
	
	--keeping the timer updated
	
	--checking if players move
	
	for i =ROUND_DURATION_SECONDS, 0, -1  do
		TimerUI.TimeLabel.Text = SecondsToTimestamp(i)
		
		if isRedLight.Value then
			--Get the position of players, check if players have moved
			for player, savedPosition in pairs(savedPlayerPositions) do
				if player.Character then
					
					local winnerIndex = table.find(winners,player)
					if winnerIndex then
						continue
					end
					
					local HumanoidRootPart = player.Character:FindFirstChild("HumanoidRootPart")
					if HumanoidRootPart then
						if(HumanoidRootPart.Position-savedPosition).Magnitude >= 1 then
							player.Character:BreakJoints() --kill the player
							savedPlayerPositions[player] = nil
							--Remove the player from the round table
							local playerIndex = table.find(playersInRound, player)
							if playerIndex then
								table.remove(playersInRound, playerIndex)
							end
						end
					end
				end
			end
		end
		
		if tick()-lastSpin >= spinDelay then --Has 5 seconds gone by since the last turn
			if isRedLight.Value == true then
				--Make it a green light
				isRedLight.Value = false
				GreenLightHead:Play()
			else
				--Make it a red light
				isRedLight.Value = true
				RedLightHead:Play()
				RedLightHead.Completed:Wait()
				LogPlayerPositions(playersInRound)
			end
			lastSpin = tick()
			spinDelay = spinDelay * 0.95 -- Make it 10% faster each time
		end
		 
		if #playersInRound == 0 then
			break
		end
		task.wait(1) --Important
	end
	
	--by this time, the game is over
	endTouch:Disconnect()
	
	for _, winner in pairs(winners) do
		
		winner.leaderstats.Cash.Value +=5
		if winner.Character then
			
		end
	end
	
	print("Round Over!")
	
end

--Main game loop
while true do
	print("Waiting 5 seconds before starting a new game.")
	task.wait(5)
	StartGame()
end

