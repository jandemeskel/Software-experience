# Global Variables #
operators = ['+', '-', '/', '*','%', '^', '']
stack = []
max_number = 2147483647
min_number = -2147483647

# Generalized function which evaluates an equation for a given operator and two given operands #
def evaluate(a,b, operator):
  
  if operator == '+':
    result = a + b
  elif operator == '-':
    result = a - b
  elif operator == '/':
    result = a / b
  elif operator == '*':
    result = a * b
  elif operator == '^':
    result = a ** b
  elif operator == '%':
    result = a % b

  else:
    return 0

  return result

# Function containing the main calculator stack functionailty #
def compute_stack(): 

# error handling, this ensures the programme doesn't crash #

 try:

   # assign terminal input to equation string variable #
    eq_string = input()
  
    # if only 1 value contained within the stack and an operator is added, state stack is underflown #

    if eq_string in operators and len(stack) < 2:
      print('Stack underflow')
  
    # if input is an operator and the above if statement is not satisifed#
    elif eq_string in operators:
      
      # top of the stack is the last value appended to the stack array #
      # operand at the start of an equation is the second to top value appended to the stack array #
      top_stack = stack[-1]
      next_stack = stack[-2]
      
      # nested if loop within elif #
      # outer loop => if input is an operator #
      # inner loop => if operator is divide and zero  is the denominator, print statement divide by zero to make the user aware"

      if top_stack == 0 and eq_string == '/':
        print("Divide by zero")
      
      # inner loop => if statement above is not satisified continue by evaluating equation, by calling upon function defined outside #
      else:
      
        eq_evaluate = evaluate(next_stack, top_stack, eq_string)
        
        # set of further nested if loop, used to ensure stack numbers never execede range of numbers, where the size of range defined is equal to the maximum 32 bit number (2^32)#

        if eq_evaluate > max_number:

          result = max_number
          stack.pop()
          stack.pop()
          stack.append(result)
    
        elif eq_evaluate < min_number:

          result = min_number
          stack.pop()
          stack.pop()
          stack.append(result)
    
        else:
          result = eq_evaluate
          stack.pop()
          stack.pop()
          stack.append(result)

    # special if case to add calculator functionality: if d is entered as an input, display the current stack #

    elif eq_string == 'd':
      for stack_element in range(len(stack)):
        print(stack[stack_element])
    
    # special if case to add calculator functionality: if = is entered as an input, display result of the last operation equivalent to value at the top of the stack, if no operations have occured the top of the stack is still returned #

    elif eq_string == '=':
      print(stack[-1])

    # given if input is not an operator or the special calculator functionality letters and the input is an integer, add the input to the stack only if the stack size limit has not been met #
    
    else:
      if len(stack) < 24:
        if int(eq_string) <= max_number and int(eq_string) >= min_number:
          stack.append(int(eq_string))
        elif int(eq_string) > max_number:
          stack.append(max_number)
        elif int(eq_string) < min_number:
          stack.append(min_number)
      else:
        print('stack overflow')
 
 # if input is not valid the following expection statement is given #
 except:
   print('Unrecognised operator or operand "{}"'.format(eq_string))

 return 0

# Message to display programme has initialized successfully #
print("You can now start interacting with the SRPN calculator")

# Infinite loop to ensure the programme continues to run #
while True:
  compute_stack()
