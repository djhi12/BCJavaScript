--[[
    Lua's :FindFirstChild() method is used to search for a child instance of a parent instance in Roblox game development. This method is commonly used to locate specific objects within a game hierarchy so that developers can perform actions or manipulate those objects programmatically.

    The :FindFirstChild() method takes a single argument, which is the name of the child instance being searched for. It returns a reference to the first child instance found with the given name, or nil if no such child instance is found.    
--]]


-- Here's an example of how to use :FindFirstChild() in a script:
-- Assume a Part object named "MyPart" exists as a child of the Workspace object.
local workspace = game:GetService("Workspace")
local myPart = workspace:FindFirstChild("MyPart")

if myPart then
    -- The MyPart object was found, so we can manipulate it.
    myPart.Size = Vector3.new(2, 2, 2)
else
    -- The MyPart object was not found, so we can't do anything with it.
    print("MyPart not found!")
end

-- In this example, the script first gets a reference to the Workspace object using the game:GetService() method. It then calls :FindFirstChild() on the Workspace object, passing in the string "MyPart" as the child instance name to search for. If the method returns a non-nil value, indicating that the child instance was found, the script sets the Size property of the MyPart object to a new Vector3 value. Otherwise, the script simply prints a message to the console indicating that the object was not found.