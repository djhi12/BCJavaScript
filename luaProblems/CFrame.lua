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

--[[
local part = Instance.new("Part"): This line creates a new instance of a "Part" object using the Instance.new() function. The Part class represents a basic building block in the Roblox platform.

part.Size = Vector3.new(2, 2, 2): Here, the Size property of the part is set to a Vector3 value of (2, 2, 2), which sets the dimensions of the part.

part.Anchored = true: The Anchored property of the part is set to true, which means the part will not move due to physics or external forces.

part.Position = Vector3.new(0, 5, 0): The Position property of the part is set to a Vector3 value of (0, 5, 0), which determines the initial position of the part in 3D space.

part.Parent = workspace: The Parent property of the part is set to the workspace, which is a container that holds objects in a Roblox game.

local radius = 5 and local speed = 1: These lines define two variables, radius and speed, that determine the parameters for the circular motion animation. The radius represents the distance from the center of the circle, and the speed determines the angular velocity of the animation.

while true do: This initiates an infinite loop, ensuring that the animation keeps running until the program is interrupted or stopped.

for angle = 0, 2*math.pi, speed do: This for loop iterates through angles from 0 to 2*math.pi (a full circle) with a step size of speed.

local x = math.cos(angle) * radius and local z = math.sin(angle) * radius: These lines calculate the x and z coordinates of a point on the circumference of the circle using trigonometric functions (cos and sin) and the current angle and radius.

local cf = CFrame.new(x, 5, z): This creates a new CFrame object at the circular position specified by the calculated x and z coordinates and a fixed y-coordinate of 5.

part.CFrame = cf: The CFrame object cf is assigned to the CFrame property of the part, updating its position and rotation.

wait(0.01): This pauses the animation for a short duration of 0.01 seconds, controlling the speed of the animation.

By continuously updating the part's CFrame within the animation loop, the part appears to move in a circular path around the initial position specified in step 4. The animation continues indefinitely due to the infinite loop in step 7.	
--]]
