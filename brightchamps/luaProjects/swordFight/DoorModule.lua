local module = {}

local tweenService = game:GetService("TweenService") --[[ The TweenService is a built-in service provided by the Roblox game engine, which allows developers to create smooth transitions between different states or properties of objects in a game. For example, using TweenService, developers can smoothly animate the movement of a character or the scaling of an object over a specified period of time.

In this code, the game:GetService() function is called to retrieve the TweenService object from the game engine. The local keyword is used to declare a variable named tweenService and assign the retrieved TweenService object to it.

This code snippet is often used at the beginning of a script that requires the TweenService object, so that it can be easily accessed and used throughout the rest of the script.	
--]]


function module.swingDoor(angle,door) -- The function takes two arguments: the angle to swing the door by, and a reference to the door object in the game world.
  
    local hingeBefore = door.CFrame * CFrame.new(-2.5, 0, 0) -- The code then locates the hinge of the door. It does this by taking the current position and orientation of the door, and then applying a translation (using CFrame.new) to move the hinge location to a fixed offset from the door's origin.

   
    local relative = hingeBefore:toObjectSpace(door.CFrame) -- Next, the code calculates the current position of the door relative to the hinge. It does this by transforming the current position of the door into the coordinate space of the hinge using toObjectSpace.

   
    local hingeAfter = hingeBefore * CFrame.Angles(0, math.rad(angle), 0) -- The hinge is then rotated around the Y-axis by the specified angle (converted from degrees to radians using math.rad), using the Angles method of the CFrame class.

	local tweenProperties = TweenInfo.new(0.2) -- TweenInfo is used to define the length of the transition (0.2 seconds in this case), and Create is used to create the tween object.

	local result = {CFrame = hingeAfter:toWorldSpace(relative)} -- The door is then repositioned relative to the new hinge location by applying the relative position offset calculated earlier to the new hinge location, and transforming it back into the world coordinate space using toWorldSpace.
	
	door.CanCollide = false -- The CanCollide property of the door is set to false, which allows the door to pass through other objects during the tween transition.
	
	local tween = tweenService:Create(door,tweenProperties,result) -- A Tween is created to smoothly transition the door's position and orientation from its current location to the new position and orientation specified by result. TweenInfo is used to define the length of the transition (0.2 seconds in this case), and Create is used to create the tween object.

	tween:Play() -- The Tween is played, causing the door to smoothly move and rotate to its new position and orientation over the specified duration.
	
	wait(0.2) -- The function then waits for 0.2 seconds (the length of the tween transition) using wait.
	
	door.CanCollide = true -- Finally, the CanCollide property of the door is set back to true, causing the door to once again interact with other objects in the game world.
end

function module.ActivateDoors(doorFolder)
	for _, door in pairs(doorFolder:GetChildren()) do
		if door:FindFirstChild("Key") then
			
			door.Touched:Connect(function(hit)
				if hit.Parent:FindFirstChild("Key") then
					if door.Key.Value == hit.Parent.Name then
						if door.Name == "ExitDoor" then
							if door.Generator.On.Value == true and not door:FindFirstChild("WoodBlock") then
								door.Padlock.Anchored = false
								wait(1)
								door.Transparency = 1
								door.CanCollide = false
								
								door.Touched:Connect(function(hit)
									
									local player = game.Players:GetPlayerFromCharacter(hit.Parent)
									
									if player then
										if player:FindFirstChild("Contestant") and not player:FindFirstChild("Escaped") then
											
											local Escaped = Instance.new("BoolValue")
											Escaped.Name = "Escaped"
											Escaped.Parent = player
											
											game.ReplicatedStorage.Announcement:FireClient(player,"You Escaped")
											
										end
									end
									
										
								end)
								
							end
						else
							door.Padlock.Anchored = false
							wait(0.5)
							door:Destroy()
						end
					end
				end
			end)
		
		else
			if not door:FindFirstChild("ClickDetector") then local cd = Instance.new("ClickDetector") cd.Parent = door end
			
			local debounce = false
			
			door:FindFirstChild("ClickDetector").MouseClick:Connect(function(player)
				
				if door.Name == "Door" then
					if not debounce then
						debounce = true
						
						local angle
						
						if door:FindFirstChild("Open") then
							angle = -90
							door.Open:Destroy()		
						else
							angle = 90	
							local openVal = Instance.new("StringValue")
							openVal.Name = "Open"
							openVal.Parent = door
						end
						
					
						module.swingDoor(angle,door)
						wait(.001)
						
						
						print("Door swung!")
						wait(1)
						debounce = false
					end
				end
			
			end)
		end
	end
end

return module