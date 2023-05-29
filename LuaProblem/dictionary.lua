-- Create a dictionary table
local dictionary = {}

-- Add key-value pairs to the dictionary
dictionary["apple"] = "a fruit"
dictionary["car"] = "a vehicle"
dictionary["sun"] = "a star"

-- Retrieve values from the dictionary
local fruitDescription = dictionary["apple"]
print("Description of 'apple':", fruitDescription)

local vehicleDescription = dictionary["car"]
print("Description of 'car':", vehicleDescription)

local starDescription = dictionary["sun"]
print("Description of 'sun':", starDescription)

-- Iterate over the key-value pairs in the dictionary
print("All entries in the dictionary:")
for key, value in pairs(dictionary) do
  print(key .. ": " .. value)
end

--[[
local dictionary = {}: This line creates an empty table named dictionary using the table constructor {}. It serves as our dictionary or associative array.

dictionary["apple"] = "a fruit": This line adds a key-value pair to the dictionary table. The key is "apple" and the corresponding value is "a fruit". This syntax uses the square brackets ([]) to access the table and assign a value to a specific key.

dictionary["car"] = "a vehicle" and dictionary["sun"] = "a star": These lines add more key-value pairs to the dictionary table in a similar manner.

local fruitDescription = dictionary["apple"]: This line retrieves the value associated with the key "apple" from the dictionary table and assigns it to the variable fruitDescription.

print("Description of 'apple':", fruitDescription): This line prints the description of the key "apple" by concatenating the string "Description of 'apple':" with the value stored in fruitDescription.

local vehicleDescription = dictionary["car"] and local starDescription = dictionary["sun"]: These lines retrieve the values associated with the keys "car" and "sun" from the dictionary table and assign them to the respective variables.

print("All entries in the dictionary:"): This line prints a heading indicating that the following lines will display all entries in the dictionary.

for key, value in pairs(dictionary) do: This line starts a loop that iterates over each key-value pair in the dictionary table using the pairs() function.

print(key .. ": " .. value): This line prints each key-value pair in the format "key: value" by concatenating the key, a colon (:), and the value using the .. concatenation operator.

In summary, the code demonstrates how to create a table and use it as a dictionary in Lua. It adds key-value pairs, retrieves values by their keys, and iterates over all entries in the dictionary to print them out.    
--]]