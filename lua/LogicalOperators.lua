-- In Lua, logical operators are used to perform logical operations on boolean values (true and false). The three logical operators in Lua are:


-- and: The and operator returns true if both its operands are true, and false otherwise. For example:
local a = true
local b = false
print(a and b) -- Output: false


-- or: The or operator returns true if at least one of its operands is true, and false otherwise. For example:
local a = true
local b = false
print(a or b) -- Output: true


-- not: The not operator returns the opposite of its operand. If the operand is true, it returns false, and if the operand is false, it returns true. For example:
local a = true
print(not a) -- Output: false

-- These logical operators are useful for creating complex conditions in if-then statements, while loops, and other control structures.