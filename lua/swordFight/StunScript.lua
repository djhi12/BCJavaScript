local debounce = false

game.ReplicatedStorage.Stun.OnServerEvent:Connect(function(plr,target)
	if target then
		if target:FindFirstAncestorOfClass("Model") then
			-- Check to see if clicked model is a real player
			local pig = game.Players:GetPlayerFromCharacter(target:FindFirstAncestorOfClass("Model"))
			
			if pig then
				if pig:FindFirstChild("Piggy") then -- Check to see if it is actually Piggy or just another contestant
					if not debounce then
						
						local stunTag = Instance.new("BoolValue") -- Add stun tag so that we can check in other scripts such as Piggy Bat script whether Piggy is stunned or not
						stunTag.Name = "Stunned"
						stunTag.Parent = pig
						
						if pig.Character:FindFirstChild("Head") then
							-- Add confusion sparkles to show Piggy is stunned
							local Sparkles = Instance.new("Sparkles")
							Sparkles.Parent = pig.Character:FindFirstChild("Head")
							Sparkles.SparkleColor = Color3.fromRGB(255,255,255)
						end
						
						-- Announce to all players in GUI that Piggy is stunned
						
						game.ReplicatedStorage.Announcement:FireAllClients("Piggy is gone for 20 seconds")
						-- Enable debounce so stun effect cannot be applied again for 20 seconds
						debounce = true
						-- Freeze pig by setting walkspeed to 0
						pig.Character.Humanoid.WalkSpeed = 0
						wait(20) -- wait 20 sec before enabling walkspeed again to 14 and then setting debounce to false so
						-- that the piggy can be stunned again
						pig.Character.Humanoid.WalkSpeed = 14
						debounce = false
						-- At the end of the debounce, remove sparkles
						if pig.Character then
							if pig.Character:FindFirstChild("Head"):FindFirstChild("Sparkles") then
								pig.Character:FindFirstChild("Head"):FindFirstChild("Sparkles"):Destroy()
							end
						end
						
						pig:FindFirstChild("Stunned"):Destroy() -- Delete stunned tag so we can tell from other scripts that the
						-- piggy is no longer stunned.
					end
				end
			end		
		end
	end
end)