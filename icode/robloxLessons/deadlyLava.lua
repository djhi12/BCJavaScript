--local lava = game.Workspace.DeadlyLavaFolder.LavaPool

--local function killPlayer(otherPart)
--	local partParent = otherPart.Parent
--	local humanoid = partParent:FindFirstChild("Humanoid")
--	if humanoid then
--		humanoid.Health = 0
--	end
--end

--lava.Touched:Connect(killPlayer)


local lava = game.Workspace.DeadlyLavaFolder.LavaPool -- This line declares a new local variable called lava and sets it to the value of the LavaPool object in the DeadlyLavaFolder in the game's workspace.

local function killPlayer(otherPart) -- This line declares a new local function called killPlayer with a single parameter otherPart.

	local character = otherPart.Parent:FindFirstAncestorOfClass("Model") -- This line declares a new local variable called character and sets it to the first ancestor of the otherPart parameter that is a Model.

	if character and character:FindFirstChild("Humanoid") then -- This line starts an if statement. If character exists and has a child object named "Humanoid", then the code inside the if statement will be executed.

		character.Humanoid.Health = 0 -- This line sets the Health property of the Humanoid object inside the character object to 0, effectively killing the player's character.
	end
end -- This line ends the if statement.

lava.Touched:Connect(killPlayer) -- This line connects the Touched event of the lava object to the killPlayer function. This means that whenever something touches the lava object, the killPlayer function will be called with the touching object's otherPart parameter.