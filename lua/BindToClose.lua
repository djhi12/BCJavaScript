--[[
BindToClose() is a function in Lua that is used in Roblox game development to register a function that will be called when the game is closed, either by the player leaving the game or by shutting down the server.

The BindToClose() function takes one argument, which is a function that will be called when the game is closing. This function will be executed before the game is shut down, so it is commonly used to save data or perform other cleanup tasks.    

--]]

-- Here is an example of how to use BindToClose():
function onGameClose()
    -- save game data
    print("Game is closing")
 end
 
 game:BindToClose(onGameClose)

-- In this example, the onGameClose() function will be called when the game is closing, and it will save the game data and print a message to the console. The game object is a reference to the Roblox game instance, and the BindToClose() function is called on this object to register the onGameClose() function to be called when the game is closing.