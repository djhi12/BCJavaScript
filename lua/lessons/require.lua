--[[
    In Lua, the require function is used to load and execute external Lua modules. It takes a string argument that specifies the name of the module to be loaded, and it returns the module's return value.

    The require function searches for the module in a predefined search path, which is stored in the global package.path variable. If the module is found, it is loaded and executed, and its return value is returned by the require function. If the module is not found, require returns nil and an error message.

    Once a module is loaded by require, its return value is cached in the package.loaded table, so that subsequent calls to require with the same module name will return the cached value instead of reloading the module.    
--]]


-- Here is an example of using require to load and use an external module:
-- Load the "math" module
local math = require("math")

-- Use a function from the module
print(math.sin(0)) -- prints "0"


