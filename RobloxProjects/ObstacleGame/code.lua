-- Obstacle Game

local player = game.Players.LocalPlayer
local character = player.Character or player.CharacterAdded:Wait()
local humanoid = character:WaitForChild("Humanoid")

-- Configure player movement
local walkSpeed = 16 -- Adjust as needed

-- Detect player input
local userInputService = game:GetService("UserInputService")
local isJumping = false

-- Function to handle player movement
local function onKeyPress(input)
	if input.KeyCode == Enum.KeyCode.W then
		humanoid:MoveTo(humanoid.RootPart.Position + humanoid.MoveDirection * walkSpeed)
	
    elseif input.KeyCode == Enum.KeyCode.Space then
		if not isJumping then
			humanoid:ChangeState(Enum.HumanoidStateType.Jumping)
			isJumping = true
		end
	end
end

-- Connect input events
userInputService.InputBegan:Connect(onKeyPress)

-- Handle jump completion
humanoid.StateChanged:Connect(function(oldState, newState)
	if newState == Enum.HumanoidStateType.Landed then
		isJumping = false
	end
end)


--[[
Checkpoints and Progress Tracking:
Place invisible checkpoints throughout the obstacle course using Parts.
Create a script to detect when the player reaches a checkpoint and update their progress.
--]]

local checkpoints = {} -- List of checkpoints in the course

-- Function to check if a player has reached a checkpoint
local function checkCheckpoint(player, checkpointPart)
	-- Assuming you have a leaderboard with the 'Checkpoint' value
	local leaderstats = player:WaitForChild("leaderstats")
	local checkpointValue = leaderstats:FindFirstChild("Checkpoint")

	-- Update the player's checkpoint value
	if checkpointValue then
		checkpointValue.Value = checkpointPart.Name
	end
end

-- Connect checkpoint detection to parts
for _, checkpointPart in ipairs(checkpoints) do
	checkpointPart.Touched:Connect(function(hitPart)
		local player = game.Players:GetPlayerFromCharacter(hitPart.Parent)
		if player then
			checkCheckpoint(player, checkpointPart)
		end
	end)
end


--[[
	Win Condition:
Create a script to check if the player has completed the obstacle course.
--]]


-- Assuming you have a 'Finish' part at the end of the course
local finishPart = workspace.Finish

-- Function to check if the player has completed the course
local function checkCourseCompletion(player)
	local leaderstats = player:WaitForChild("leaderstats")
	local checkpointValue = leaderstats:FindFirstChild("Checkpoint")

	if checkpointValue and checkpointValue.Value == finishPart.Name then
		-- Player has completed the course, implement win condition
		-- ...
	end
end

-- Check course completion when a player touches the finish part
finishPart.Touched:Connect(function(hitPart)
	local player = game.Players:GetPlayerFromCharacter(hitPart.Parent)
	if player then
		checkCourseCompletion(player)
	end
end)
