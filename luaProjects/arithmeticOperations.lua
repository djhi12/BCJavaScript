-- Function to perform addition
function add(a, b)
    return a + b
  end
  
  -- Function to perform subtraction
  function subtract(a, b)
    return a - b
  end
  
  -- Function to perform multiplication
  function multiply(a, b)
    return a * b
  end
  
  -- Function to perform division
  function divide(a, b)
    -- Check for division by zero
    if b == 0 then
      return "Error: Division by zero"
    else
      return a / b
    end
  end
  
  -- Testing the functions
  print("3 + 4 = ", add(3, 4))
  print("10 - 5 = ", subtract(10, 5))
  print("2 * 8 = ", multiply(2, 8))
  print("10 / 2 = ", divide(10, 2))
  print("6 / 0 = ", divide(6, 0))

  --[[
    In this program, we define four functions: add, subtract, multiply, and divide. Each function takes two arguments (a and b) and returns the result of performing the corresponding arithmetic operation on those arguments.

    We then test the functions by calling them with different arguments and printing the results. The divide function includes an additional check to handle division by zero, which returns an error message in that case.  
  --]]