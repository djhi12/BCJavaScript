--[[
    In Roblox Studio, the Explorer window allows you to view and edit various aspects of your game, including the Lighting settings.

    The Lighting object in the Explorer represents the lighting settings of your game. You can access it by clicking on it in the Explorer window, or by going to the View tab and selecting Lighting.

    Inside the Lighting object, you can adjust various settings such as the ambient light color and brightness, the sun and moon settings, and the fog properties. These settings can have a significant impact on the look and feel of your game.

    For example, you can change the color of the ambient light to create a certain mood or atmosphere, or adjust the fog properties to create a sense of depth and distance. You can also adjust the sun and moon settings to change the time of day in your game.

    Overall, the Lighting object in the Explorer window is a powerful tool that allows you to control the lighting and atmosphere of your game, and can help you create a more immersive and engaging experience for your players.    
--]]


--[[
    In addition to using the Explorer window to adjust the Lighting settings, you can also access and modify these settings through code using the Roblox Lua programming language.

    Here are some examples of how you can use code to modify the Lighting settings:    
--]]

-- Changing the ambient color:
game:GetService("Lighting").AmbientColor = Color3.fromRGB(255, 255, 255)

-- This code changes the ambient color of the game's Lighting to white (RGB value of 255, 255, 255).


-- Adjusting the sun's position:
game:GetService("Lighting").ClockTime = 8
game:GetService("Lighting").GeographicLatitude = 40.7
game:GetService("Lighting").GeographicLongitude = -74

-- This code sets the time of day to 8 AM, and sets the latitude and longitude of the sun's position to correspond to the location of New York City.


-- Changing the fog properties:
game:GetService("Lighting").FogEnd = 100
game:GetService("Lighting").FogColor = Color3.fromRGB(200, 200, 200)

-- This code sets the distance at which the fog starts to 0 and the distance at which it completely obscures objects to 100. It also sets the color of the fog to a light gray color.


--[[
    By using code to modify the Lighting settings, you can create more dynamic and interactive experiences in your game.    
--]]