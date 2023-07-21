--[[    
In Roblox Studio, a "local script" is a type of script that runs on the client-side, meaning it executes on each player's computer rather than on the server. Local scripts are commonly used to create client-side game mechanics, user interfaces, and other features that do not require server interaction.

Here's a brief overview of how local scripts work and how they are used in Roblox Studio:

Creating a Local Script:
To create a local script in Roblox Studio, follow these steps:
Open the Explorer window (usually on the right side of the screen).
Right-click on the "Workspace" or any other desired location (e.g., StarterPlayerScripts, StarterCharacterScripts, etc.).
Go to "Insert Object" and select "LocalScript."
The local script will appear in the Explorer and be ready for editing.

Writing Code in a Local Script:
Once you have created a local script, you can double-click on it to open the code editor. Here, you can write Lua code to define the behavior of the client-side features you want to implement.


Running the Local Script:
When you run the game in Roblox Studio, each player who joins the game will execute the local script on their client-side. This means that the code inside the local script will be executed independently for each player.

Keep in mind that local scripts cannot directly interact with the server or modify the game's state in a way that affects other players. If you need to perform actions that involve server communication or global changes, you would need to use a "Script" object (also known as a "server script") instead.

Additionally, local scripts can be used in conjunction with "RemoteEvents" and "RemoteFunctions" to communicate between the client and server securely. This allows you to send messages and data back and forth between the client and server scripts while maintaining security and preventing cheating.

Remember, client-side scripts are not authoritative, meaning players can potentially manipulate them to cheat or exploit the game. Always validate important actions on the server to ensure the integrity of your game.

--]]


-- Example Program
-- Get references to the part and the button
local part = game.Workspace.Part
local button = script.Parent

-- Function to change the color of the part
local function changeColor()
    local newColor = Color3.new(math.random(), math.random(), math.random())
    part.BrickColor = BrickColor.new(newColor)
end

-- Connect the button's Click event to the changeColor function
button.MouseButton1Click:Connect(changeColor)
