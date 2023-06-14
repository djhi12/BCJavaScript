--[[
    In Lua, the return keyword is used to exit a function and return a value or a set of values to the caller.

    When a return statement is executed within a function, the function is terminated immediately, and the control is passed back to the calling function. The value or values specified after the return keyword are returned as the result of the function call.    
--]]

-- Here is an example:
-- A simple function that adds two numbers and returns the result
function addNumbers(a, b)
    return a + b
  end
  
  -- Call the function and store the result in a variable
  local result = addNumbers(3, 5)
  
  -- Print the result
  print(result) -- Output: 8

--[[
    In this example, the addNumbers function takes two arguments and returns their sum using the return statement. The result variable is assigned the value returned by the function, which is then printed to the console.

    In addition to returning a single value, Lua functions can also return multiple values separated by commas. Here is an example:    
--]]

-- A function that returns multiple values
function getMinMax(numbers)
    local min = math.huge
    local max = -math.huge
    
    for _, n in ipairs(numbers) do
      if n < min then min = n end
      if n > max then max = n end
    end
    
    return min, max
  end
  
  -- Call the function and store the results in variables
  local minVal, maxVal = getMinMax({10, 20, 5, 15, 30})
  
  -- Print the results
  print("Minimum value:", minVal) -- Output: Minimum value: 5
  print("Maximum value:", maxVal) -- Output: Maximum value: 30

-- In this example, the getMinMax function takes a table of numbers as an argument and returns the minimum and maximum values in the table as separate return values. The values are then stored in separate variables and printed to the console.