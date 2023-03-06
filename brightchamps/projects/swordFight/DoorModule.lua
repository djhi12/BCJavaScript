local module = {}

local tweenService = game:GetService("TweenService")

-- swing the door by `angle` degrees
function module.swingDoor(angle,door)
    -- locate the hinge on the door
    local hingeBefore = door.CFrame * CFrame.new(-2.5, 0, 0)

    -- relative to the hinge, where is the door?
    local relative = hingeBefore:toObjectSpace(door.CFrame)

    -- twist the hinge
    -- CONVERT angle *from* degrees *to* radians here
    local hingeAfter = hingeBefore * CFrame.Angles(0, math.rad(angle), 0)

    -- re-attach the door to the new "hinge"

	local tweenProperties = TweenInfo.new(0.2) -- Time
	local result = {CFrame = hingeAfter:toWorldSpace(relative)}
	
	door.CanCollide = false
	
	local tween = tweenService:Create(door,tweenProperties,result)
	tween:Play()
	
	wait(0.2)
	
	door.CanCollide = true
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