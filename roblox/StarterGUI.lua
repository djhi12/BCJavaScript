--[[
	In Roblox Studio, the StarterGUI is a special object that allows you to create a user interface for your game. When a player joins your game, the StarterGUI is loaded and displayed on their screen.

	To create a StarterGUI in Roblox Studio, follow these steps:

		1. Open Roblox Studio and create a new place or open an existing one.

		2. In the Explorer window, select the Workspace object.

		3. Right-click the Workspace object and select Insert Object > ScreenGui.

		4. Rename the ScreenGui to "StarterGui" (note the capitalization) to make it a StarterGUI object.

		5. With the StarterGui selected, you can now add UI elements to it using the Insert menu. Common UI elements include frames, text labels, buttons, and images.
			
		6. Once you've added UI elements, you can customize their properties by selecting them and modifying the properties in the Properties window.

	When a player joins your game, the StarterGUI will be loaded and displayed on their screen. You can use scripting to make the UI elements interactive and respond to player input. For example, you might use a button to open a settings menu or a text box to allow the player to enter their name.

	Overall, the StarterGUI is a powerful tool that allows you to create a custom user interface for your Roblox game. With some creativity and scripting know-how, you can create a polished and professional-looking UI that enhances the player experience.
--]]

-- To use the StarterGUI in code, you can first retrieve it using the StarterGui service, which provides access to the player's starter GUI.

-- Retrieve the StarterGui service
local StarterGui = game:GetService("StarterGui")

-- Create a new TextLabel instance
local myLabel = Instance.new("TextLabel")
myLabel.Text = "Hello, world!"
myLabel.Size = UDim2.new(0, 200, 0, 50)
myLabel.Position = UDim2.new(0.5, -100, 0.5, -25)

-- Add the TextLabel to the StarterGUI
myLabel.Parent = StarterGui.ScreenGui

--[[
	In this example, we first retrieve the StarterGui service using the game:GetService() method. Then, we create a new TextLabel instance and set its properties as desired. Finally, we add the TextLabel to the ScreenGui object within the StarterGui by setting its Parent property to StarterGui.ScreenGui.

	You can use a similar approach to add other GUI elements to the StarterGUI, or to modify existing elements that are already present. Additionally, you can use events and callback functions to handle user input and update the GUI dynamically based on game events or other conditions.	
--]]
