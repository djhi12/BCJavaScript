--[[
Roblox Studio is a powerful development tool used for creating games and experiences on the Roblox platform. Within Roblox Studio, you have the ability to customize various aspects of your game, including the chat system.

The chat system in Roblox allows players to communicate with each other using text-based messages. It is a vital component for multiplayer games and social experiences on the platform. As a developer, you can control how the chat system works and customize its functionality to suit your game's needs.

Here are some key points to consider when working with the chat system in Roblox Studio:

Chat Service: The chat functionality in Roblox is managed by the Chat service, which provides APIs for sending and receiving messages. You can access the Chat service through the Chat module in Lua scripting.

Filtering Enabled: Roblox enforces a feature called "Filtering Enabled" to prevent inappropriate content and protect players. When Filtering Enabled is enabled, all messages sent by players go through a content filter to ensure compliance with Roblox's guidelines.

Sending Messages: You can use the Chat:Chat method to send messages to players. Messages can be sent to specific players or broadcasted to all players in the game. You can also customize the appearance of the messages, such as font style, color, and size.

Filtering and Moderation: Roblox provides a built-in moderation system to filter and moderate chat messages. This helps maintain a safe and appropriate environment for players. You can configure the moderation settings for your game through the Roblox website.

Chat GUI: The appearance and functionality of the chat user interface (UI) can be customized to match the theme and style of your game. You can design your own chat UI using the Studio's GUI editor or utilize existing chat UI templates available in the Roblox library.

Chat Commands: You can implement custom chat commands that trigger specific actions within your game. For example, players can type "/dance" in the chat to make their character perform a dance animation.

Chat Events: Roblox provides various events that allow you to listen for chat-related actions. For example, the ChatService.OnMessage event is triggered when a player sends a chat message, allowing you to perform certain actions based on the content of the message.

These are just a few aspects of working with the chat system in Roblox Studio. By leveraging the Chat service and utilizing the available APIs, you can create engaging and interactive chat experiences for your players.    
--]]


-- Example Program
-- Get the Chat service
local ChatService = game:GetService("Chat")

-- Function to handle player chat
local function onPlayerChatted(player, message)
    -- Print the player's name and their message
    print(player.Name .. " says: " .. message)
end

-- Connect the onPlayerChatted function to the OnMessage event
ChatService.OnMessage:Connect(onPlayerChatted)

--[[
In this example, we first retrieve the Chat service using game:GetService("Chat"). Then, we define a function called onPlayerChatted that takes two parameters: player (the player who sent the chat message) and message (the content of the message).

Inside the onPlayerChatted function, we simply print the player's name and their message to the output console using print(). You can modify this function to perform any other actions you desire based on the received chat messages.

Finally, we connect the onPlayerChatted function to the OnMessage event of the Chat service using ChatService.OnMessage:Connect(onPlayerChatted). This ensures that the onPlayerChatted function is called whenever a player sends a chat message.

Remember to place this script in a server-side script object in Roblox Studio. It will allow you to see the chat messages in the output console when you run the game. You can further enhance this example by incorporating filtering and moderation features provided by the Chat service to ensure a safe and appropriate chat environment for your players.    
--]]