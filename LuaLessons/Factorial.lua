-- In Lua, you can write a function to calculate the factorial of a given number using recursion. 
function factorial(n)
    if n == 0 then
        return 1
    else
        return n * factorial(n - 1)
    end
end

-- In this function, we check if the input n is equal to 0. If it is, we return 1 (because the factorial of 0 is 1). If n is not equal to 0, we recursively call the factorial function with n - 1 as the input and multiply the result with n. This continues until n becomes 0 and the function returns 1.

print(factorial(5)) -- Output: 120

-- This will calculate and print the factorial of 5, which is 5 x 4 x 3 x 2 x 1 = 120.