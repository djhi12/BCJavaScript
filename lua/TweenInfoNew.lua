--[[
    In Lua, TweenInfo.new() is a function that creates a new TweenInfo object. A TweenInfo object is used to specify properties for a Tween object, which is used to animate a property of a Roblox object over a certain amount of time.    
--]]

-- Here's an example of how to use TweenInfo.new():
local tweenInfo = TweenInfo.new(
    1,           -- time: the length of the tween in seconds
    Enum.EasingStyle.Linear,  -- easingStyle: the style of easing to use
    Enum.EasingDirection.Out, -- easingDirection: the direction of easing to use
    0,           -- repeatCount: the number of times to repeat the tween (0 means don't repeat)
    false,       -- reverses: whether the tween should reverse after completing a cycle
    0            -- delayTime: the amount of time to wait before starting the tween
)

-- The above example creates a TweenInfo object with a length of 1 second, a linear easing style,
-- an easing direction of "out", no repeat count, no reversing, and no delay.

-- The TweenInfo object created by TweenInfo.new() can be passed as an argument to the TweenService:Create() method, which creates a new Tween object. The Tween object can then be used to animate a property of a Roblox object over the specified time and with the specified easing style and direction.