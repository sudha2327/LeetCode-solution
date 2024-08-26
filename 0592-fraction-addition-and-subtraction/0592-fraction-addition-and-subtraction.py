from math import gcd

class Solution:
    def fractionAddition(self, expression: str) -> str:
        # Initialize numerator and common denominator
        numerator, common_denominator = 0, 1
        for d in range(2, 11):
            common_denominator *= d  # LCM(1,2,3,4,5,6,7,8,9,10)
      
        # Ensure the first character is a sign
        if expression[0].isdigit():
            expression = '+' + expression
      
        # Process each fraction in the string
        i, expr_length = 0, len(expression)
        while i < expr_length:
            # Determine the sign of the fraction
            sign = -1 if expression[i] == '-' else 1
            i += 1  # Move past the sign character
          
            # Find the end of the current fraction
            j = i
            while j < expr_length and expression[j] not in '+-':
                j += 1
          
            # Extract the current fraction
            fraction_str = expression[i:j]
            numerator_str, denominator_str = fraction_str.split('/')
          
            # Update the combined numerator
            numerator += sign * int(numerator_str) * common_denominator // int(denominator_str)
          
            # Move to the start of the next fraction
            i = j
      
        # Reduce the fraction by the greatest common divisor
        common_divisor = gcd(numerator, common_denominator)
        numerator //= common_divisor
        common_denominator //= common_divisor
      
        # Return the reduced fraction as a string
        return f'{numerator}/{common_denominator}'