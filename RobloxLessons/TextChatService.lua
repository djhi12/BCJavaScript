--[[
In Roblox Studio, the "TextChatService" is a module that provides functionality for handling in-game text chat. It allows developers to create chat systems, filter and moderate messages, and implement custom chat features within their Roblox games.

The TextChatService module provides a set of functions and events that developers can use to interact with the chat system. Some of the commonly used functions include:

TextChatService:Chat - This function is used to send a chat message to the game's chat system. Developers can specify the recipient, message content, and other parameters.

TextChatService:RegisterChatCallback - This function allows developers to register a callback function that will be triggered when a chat message is received. The callback function can be used to process and handle incoming messages.

TextChatService:FilterStringAsync - This function is used to filter a chat message string and check it against the game's chat filter settings. Developers can use this to prevent the use of inappropriate language or content in chat messages.

The TextChatService module also provides events such as TextChatService.SpeakerAdded and TextChatService.SpeakerRemoved, which allow developers to track when a player starts or stops using the chat system.

By utilizing the TextChatService module, developers can create custom chat features, implement chat moderation systems, and enhance the overall chat experience in their Roblox games.    
--]]


-- Example Program
local TextChatService = game:GetService("TextChatService")

-- Function to handle incoming chat messages
local function HandleChatMessage(speaker, message, channel)
    print(string.format("[%s][%s]: %s", channel, speaker.Name, message))
end

-- Register the chat callback
TextChatService:RegisterChatCallback(Enum.ChatCallbackType.OnMessageReceived, HandleChatMessage)

-- Function to send a chat message
local function SendChatMessage(player, message)
    TextChatService:Chat(player, message, Enum.ChatColor.Blue)
end

-- Example usage: sending a chat message
local player = game.Players.LocalPlayer
SendChatMessage(player, "Hello, everyone!")

-- Example usage: filtering a chat message
local function FilterChatMessage(message)
    local filteredMessage, isFiltered = TextChatService:FilterStringAsync(message, player.UserId)
    if isFiltered then
        print("Filtered message:", filteredMessage)
    else
        print("Original message:", message)
    end
end

-- Example usage: filtering a chat message
FilterChatMessage("I love Roblox!")

--[[
In this example, we first import the TextChatService module using game:GetService("TextChatService"). We then define a function HandleChatMessage to handle incoming chat messages. This function simply prints the message, speaker, and channel to the console.

Next, we register the chat callback using TextChatService:RegisterChatCallback. We pass in Enum.ChatCallbackType.OnMessageReceived to specify that we want to handle incoming chat messages.

We also define a function SendChatMessage to send a chat message. It uses the TextChatService:Chat function to send the message to the chat system. In this example, we're sending the message in blue color.

Lastly, we demonstrate the usage of the TextChatService:FilterStringAsync function by defining a FilterChatMessage function. This function filters a chat message and prints the filtered or original message depending on whether it was filtered.

Please note that this is a basic example to demonstrate the usage of the TextChatService module. In a real game, you would typically implement more robust chat filtering and moderation systems.    
--]]