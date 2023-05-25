"""
This module implements the calculator with two arthimatetic operations 
addition and multiplication.

The function contains one class, in which there are two functions of above operations.
The functions are being improted from arthemetic and directory.

"""

from common.constants import ERROR_VALUE
from arithemetic.product import product_fun
from arithemetic.sum import add_fun

class Calculator:
    """
    A calculator for performing operations on positive numbers.
    
    Attributes:
        error (float): The error  to be returned when input is not positive.
        name (str): The name of the calculator.
    """
    
    def __init__(self):
        """
        Initializes a new instance of the PositiveCalculator class.
        
        Sets the default error message and calculator name.
        """
        
        self.error = ERROR_VALUE
        self.name = "Positive calculator"
        


    def add_positive(num1: float, num2: float):
        """
        Adds two positive numbers together.

        Args:
            num1 (float): The first positive number.
            num2 (float): The second positive number.

        Returns:
            float: The sum of the two numbers if they are positive, otherwise returns the error.
        
         Examples:
            >>> add_positive(2, 3)
            5
            >>> add_positive(-1, 1)
            -1
        """
        if (num1 > 0 and num2 > 0):
            return add_fun(num1, num2)
        else:
            return error        
    
    def multiply_positive(num1: float, num2: float):
        """
        Multiplies two positive numbers.

        Args:
            num1 (float): The first positive number.
            num2 (float): The second positive number.

        Returns:
            float: The product of the two numbers if they are positive, otherwise returns the error message.
        
        Examples:
            >>> multiply_positive(2, 3)
            6
            >>> multiply_positive(-1, 1)
            -1
        """
        if (num1 > 0 and num2 > 0):
            return product_fun(num1, num2)
        else:
            return error       
         
        