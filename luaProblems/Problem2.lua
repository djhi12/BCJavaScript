-- Lua - "Instance.new, GetChildren, and FindFirstChild"

local function createPart()
    local part = Instance.new("Part")
    part.Name = "MyPart"
    part.Size = Vector3.new(5, 5, 5)
    part.Position = Vector3.new(0, 10, 0)
    part.BrickColor = BrickColor.new("Bright blue")
    part.Parent = workspace
end

local function printChildren(object)
    local children = object:GetChildren()
    for i, child in ipairs(children) do
        print("Child #" .. i .. ": " .. child.Name)
    end
end

local function findPartByName(name)
    local part = workspace:FindFirstChild(name)
    if part then
        print("Found part: " .. part.Name)
    else
        print("Part not found.")
    end
end

-- Main program
local workspace = game:GetService("Workspace")

createPart()

print("Children of the Workspace:")
printChildren(workspace)

findPartByName("MyPart")

--[[
In this example, the program defines three functions: createPart, printChildren, and findPartByName. The createPart function creates a new part object and adds it as a child of the Workspace. The printChildren function retrieves and prints the immediate children of a given object. The findPartByName function searches for a child with a specific name within the Workspace.

The main program then creates a part using createPart, prints the children of the Workspace using printChildren, and searches for a part named "MyPart" using findPartByName.

Remember to adjust the code and customize it based on your specific needs and game logic.    
--]]