--[[
    Lua is a dynamically typed programming language, which means that the data type of a variable is determined at runtime rather than being explicitly defined in the code. Lua supports several data types, including:

        nil - represents the absence of a value. Variables in Lua are initialized to nil by default.

        boolean - represents a boolean value (true or false).

        number - represents a numeric value. Lua supports both integer and floating-point numbers.

        string - represents a sequence of characters enclosed in quotes.

        table - represents a collection of key-value pairs. Tables can be used to implement arrays, dictionaries, and other data structures.

        function - represents a block of code that can be called with arguments.

        userdata - represents an arbitrary block of memory managed by the Lua interpreter.

        thread - represents an independent thread of execution within a Lua program.

    It's important to note that Lua is a dynamically typed language, so variables can change their data type during runtime. For example, a variable that was previously storing a string can be assigned a number later on.    
--]] 

-- Example Code
-- nil data type
local a = nil
print(type(a)) -- output: "nil"

-- boolean data type
local b = true
print(type(b)) -- output: "boolean"

-- number data type
local c = 42
print(type(c)) -- output: "number"

-- string data type
local d = "hello world"
print(type(d)) -- output: "string"

-- table data type
local e = {foo = "bar", baz = 42}
print(type(e)) -- output: "table"
print(e.foo) -- output: "bar"
print(e.baz) -- output: 42

-- function data type
local f = function(x) return x * x end
print(type(f)) -- output: "function"
print(f(3)) -- output: 9

-- userdata data type
local g = io.stdin
print(type(g)) -- output: "userdata"

-- thread data type
local function h() 
    print("hello from thread") 

end

local i = coroutine.create(h)
print(type(i)) -- output: "thread"
coroutine.resume(i) -- output: "hello from thread"

-- In this example, we declare and initialize variables of different data types, and print their types and values. We also define a function and a coroutine thread, which are examples of Lua's function and thread data types, respectively.