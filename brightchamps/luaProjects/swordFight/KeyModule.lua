local module = {}

function module.DropTool(player,map,position)
	--this function used to drop any tools that player store or equip--

	--look for tools that are in backpack--
	for i, tool in pairs(player.Backpack:GetChildren()) do
		if tool:IsA("Tool") and game.ServerStorage.KeyHandles:FindFirstChild(tool.Name) then
			local clone = game.ServerStorage.KeyHandles:FindFirstChild(tool.Name):Clone()
			--so this will clones the tool in serverstorage that has the same name


			if clone:IsA("Model") then
				clone:SetPrimaryPartCFrame(CFrame.new(position))
			else
				clone.Position = position
			end
			--so the tool will be swapped with the keyhandle that been clicked--


			clone.Parent = map.Items
			--put the keyhandle back to the Items folder

			tool:Destroy()
			--delete the previous tool from backpack--
			print("tool in backpack is switched")
		end
	end

	--look for tools that are in character--
	for i, tool in pairs(player.Character:GetChildren()) do
		if tool:IsA("Tool") and game.ServerStorage.KeyHandles:FindFirstChild(tool.Name) then
			local clone = game.ServerStorage.KeyHandles:FindFirstChild(tool.Name):Clone()

			if clone:IsA("Model") then
				clone:SetPrimaryPartCFrame(CFrame.new(position))
			else
				clone.Position = position
			end

			clone.Parent = map.Items

			tool:Destroy()
			print("tool in character")

		end
	end

end


function module.Clicked(player,item)
	print("test")
	if player.Character and not player:FindFirstChild("Piggy") then
		--so the item only can be equipped by contestants--
		
		local position
		
		if item:IsA("Model") then
			position = item.PrimaryPart.Position
		else
			position = item.Position
		end
		--this position variable used to swap the tool that you already equipped to other tools--
		--if it is a model, so the position is referenced to primarypart position
		-- it it is a part, so the position is referenced to the position itself
		

		module.DropTool(player,game.Workspace.Map,position)
		print("Dropped Tools")
		
		
		if game.ServerStorage.Tools:FindFirstChild(item.Name) then
			--make sure your keyhandle and tool have the same name--
			
			
			local clonedtool = game.ServerStorage.Tools[item.Name]:Clone()
			clonedtool.Parent = player.Backpack
			--so it clones the tool from serverstorage to player's backpack--
			
			player.Character.Humanoid:EquipTool(clonedtool)
			--player automatically equip that tool--
			
			item:Destroy()
			--so the other players can't equip it--
			
			print("Equipped the tool object")	
			
		end
	end
end

return module
