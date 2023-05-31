-- Obstacle Game


--[[
Overall, this code sets up references to the local player, their character, and the humanoid associated with that character, ensuring that these objects are available for further usage in the game's code.	
--]]
local player = game.Players.LocalPlayer
local character = player.Character or player.CharacterAdded:Wait()
local humanoid = character:WaitForChild("Humanoid")

-- Configure player movement
local walkSpeed = 16 -- Adjust as needed


-- Detect player input
--[[
Overall, this code sets up the necessary variables to handle user input and track the jumping state in a game or application.	
--]]
local userInputService = game:GetService("UserInputService")
local isJumping = false


-- Function to handle player movement
--[[
Overall, this code snippet handles keypress events. If the 'W' key is pressed, it moves the humanoid character in the game according to its current movement direction and walk speed. If the space bar is pressed and the humanoid is not already jumping, it changes the humanoid's state to jumping and sets the "isJumping" flag to true.	
--]]
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
--[[
This line connects the InputBegan event of the UserInputService to the function onKeyPress. The InputBegan event occurs when a user begins pressing a key or clicking the mouse. By connecting this event to the onKeyPress function, the code will execute the logic inside onKeyPress whenever a user starts pressing a key.	
--]]
userInputService.InputBegan:Connect(onKeyPress)


-- Handle jump completion
--[[
This code block connects the StateChanged event of the Humanoid object to an anonymous function. The StateChanged event triggers when the state of the Humanoid changes. The function takes two parameters: oldState and newState, representing the previous state and the new state, respectively.

Inside the function, there is an if statement that checks if the newState is equal to Enum.HumanoidStateType.Landed. If the condition is true, it means the Humanoid has landed, and it sets the variable isJumping to false.

In summary, the first part of the code connects the InputBegan event to the onKeyPress function to handle user input, while the second part connects the StateChanged event of the Humanoid object to detect when the character has landed and updates the isJumping variable accordingly.	
--]]
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
--[[
Overall, this code sets up event listeners for each checkpoint part, so when a player's character touches a checkpoint, the checkCheckpoint function is called, allowing for further actions or checks to be performed.	
--]]
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
