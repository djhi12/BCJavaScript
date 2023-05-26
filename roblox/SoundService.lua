--[[
In Roblox Studio, the "SoundService" is a built-in service that allows you to play sounds and manage audio in your Roblox games. It provides a range of functions and properties to control the playback, volume, and other aspects of the game's audio.

Here are some commonly used functions and properties of the SoundService in Roblox Studio:  
--]]


-- PlayLocalSound: This function allows you to play a sound locally on the client without replicating it to the server. It takes a Sound object as an argument and starts playing the sound.  
local sound = Instance.new("Sound")
sound.SoundId = "rbxassetid://123456789" -- Replace with the ID of your sound asset
sound.Parent = workspace
game.SoundService:PlayLocalSound(sound)


-- PlayLocalSoundWithParams: Similar to PlayLocalSound, this function plays a sound locally but also takes additional parameters such as volume, pitch, and time position.
local sound = Instance.new("Sound")
sound.SoundId = "rbxassetid://123456789" -- Replace with the ID of your sound asset
sound.Parent = workspace
game.SoundService:PlayLocalSoundWithParams(sound, {
    Volume = 0.5,
    Pitch = 1.2,
    TimePosition = 5,
})


-- PlayGlobalSound: This function plays a sound globally on all clients in the game. It replicates the sound to the server, which then broadcasts it to all connected clients.
local sound = Instance.new("Sound")
sound.SoundId = "rbxassetid://123456789" -- Replace with the ID of your sound asset
sound.Parent = workspace
game.SoundService:PlayGlobalSound(sound)


-- SetListener: This function sets the listener's position and orientation, affecting how sounds are spatialized in the game. It takes a Vector3 position and a Vector3 lookVector as arguments.
local player = game.Players.LocalPlayer
local character = player.Character
local humanoidRootPart = character:WaitForChild("HumanoidRootPart")
local lookVector = humanoidRootPart.CFrame.LookVector
game.SoundService:SetListener(humanoidRootPart.Position, lookVector)


-- These are just a few examples of how you can use the SoundService in Roblox Studio to manipulate audio in your games. The SoundService offers more functionality and properties for advanced audio management, such as adjusting the volume of all sounds, controlling the Doppler effect, and creating custom sound groups. You can refer to the Roblox API documentation for more details on the available functions and properties of the SoundService.