-- Create a part
local part = Instance.new("Part")
part.Size = Vector3.new(100, 100, 120)
part.Color = Color3.fromRGB(46, 49, 255)
part.Anchored = true
part.Position = Vector3.new(10, 15, 10)
part.Parent = workspace

-- Define the circular motion parameters
local radius = 5
local speed = 1

-- Animation loop
while true do
	for angle = 0, 2*math.pi, speed do
		local x = math.cos(angle) * radius
		local z = math.sin(angle) * radius
		local cf = CFrame.new(x, 5, z)  -- Create a CFrame at the circular position

		part.CFrame = cf  -- Apply the CFrame to the part

		wait(0.01)  -- Pause the animation for a short duration
	end
end
