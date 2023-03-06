--[[
    "CharacterAdded" is an event in Lua that fires whenever a new Unicode character is entered into a TextBox or a similar GuiObject.    
--]]


-- For example, let's say you have a TextBox called "myTextBox". You can use the "CharacterAdded" event to detect when a user types a new character into the TextBox, and then perform some action in response. Here's an example code snippet:
myTextBox = Instance.new("TextBox")
myTextBox.Parent = game.Players.LocalPlayer.PlayerGui

myTextBox.FocusLost:Connect(function(enterPressed)
   if enterPressed then
      print("User pressed enter!")
   end
end)

myTextBox.CharacterAdded:Connect(function(character)
   print("User typed the character:", character)
end)

--[[
    In this example, we've created a TextBox and added it to the player's GUI. We've then connected two events to it: "FocusLost" and "CharacterAdded".

    The "FocusLost" event fires when the user finishes typing in the TextBox and clicks away from it or presses the Enter key. In the example, we're using the event to check if the user pressed Enter, and if they did, we print a message to the console.

    The "CharacterAdded" event fires whenever the user types a new character into the TextBox. In the example, we're simply printing the character to the console.    
--]]