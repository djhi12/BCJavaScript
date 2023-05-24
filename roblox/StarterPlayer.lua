--[[
	In Roblox Studio, the StarterPlayer is a special object that defines the initial properties of the player's avatar when the game starts. It is a child of the StarterPack object and can be accessed through the Explorer window.

	The StarterPlayer object has several properties that can be customized to change the player's starting appearance and behavior. Some of the most commonly used properties include:

	• CharacterAppearance: This property determines the appearance of the player's avatar when the game starts. It can be set to either the default Roblox character or a custom character model.
		
	• StarterGear: This property is an array of objects that specifies the gear that the player starts with. Gear can include weapons, tools, and other items.
		
	• CanLoadCharacterAppearance: This property determines whether the player's saved appearance should be loaded when they join the game. If set to true, the player's saved appearance will be used instead of the default appearance.
		
	• ForceField: This property determines whether the player is protected by a force field when the game starts. If set to true, the player will be unable to take damage until the force field is removed.

	By customizing the properties of the StarterPlayer object, developers can create a unique and personalized experience for their players.

--]]


--[[
	To use the StarterPlayer object in your Roblox game's code, you can use the StarterPlayer module. This module provides access to the StarterPlayer object and its properties.	
--]]

-- Here's an example of how to use the StarterPlayer module to change the camera mode of your game:
-- get the StarterPlayer module
local starterPlayer = game:GetService("StarterPlayer")

-- get the StarterPlayer object
local starterPlayerObject = starterPlayer.StarterPlayer

-- set the camera mode to "Classic"
starterPlayerObject.CameraMode = Enum.CameraMode.Classic

--[[
	In this example, we use the game:GetService method to get the StarterPlayer service. Then we use the StarterPlayer service to get the StarterPlayer object by accessing the StarterPlayer property. Finally, we set the CameraMode property to Enum.CameraMode.Classic to change the camera mode of the game.

	You can use a similar approach to access and modify other properties of the StarterPlayer object. Keep in mind that some properties, such as PlayerScripts, may require more complex code to access and modify.

	It's important to note that any changes you make to the StarterPlayer object in your code will only affect players who join the game after the code is executed. Players who are already in the game will not be affected by these changes.	
--]]

