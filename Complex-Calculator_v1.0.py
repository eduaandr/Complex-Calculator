# Complex-Calculator
# Description: Program that performs complex operations with complex numbers and outputs the result in the polar format
# # Author: Eduardo Andrade
# Date: 2017/06/16
# Version: 1.0

# import numpy library for mathematical operations
import numpy as np

# define function to convert radians to degrees
def rad2deg(num1):

    # return the result
    return num1 * 180 / np.pi

# define function to convert degrees to radians
def deg2rad(num1):

    # return the result
    return num1 * np.pi / 180

# define function to convert a complex number from rectangular to polar
def rec2pol(num1,num2):

    # check if both entries are null
    if num1 == 0 and num2 == 0:

        # return the result
        return (0,0)

    # check if it is an imagine number
    elif num1 == 0 and num2 != 0:

        # return the result
        return (np.sqrt((num1)**2 + (num2)**2),90)

    # check if it is a complex number in the 3th and 4th quadrants
    elif num2 < 0:

        # return the result
        return (np.sqrt((num1)**2 + (num2)**2),rad2deg(np.arctan(num2 / num1)) - 180)

    # if not, it means it is in the 1st or 2nd quadrants
    else:

        # return the result
        return (np.sqrt((num1)**2 + (num2)**2),rad2deg(np.arctan(num2 / num1)))

# define function to perform the calculation
def polar_calculator(num1):

    # initiate the integer sum_real
    sum_real = 0

    # initiate the integer sum_imag
    sum_imag = 0

    # scans all input registries. Step of 2 necessary because num1 receives module and angle as independent inputs
    for i in range(0,len(num1) - 1,2):
        
        # perform the addition of real part
        sum_real += num1[i] * np.cos(deg2rad(num1[i + 1]))

        # perform the addition of imaginary part
        sum_imag += num1[i] * np.sin(deg2rad(num1[i + 1]))

    # print the result
    print("%.3f \u2220 %.2f\u00B0" % rec2pol(sum_real,sum_imag))
    
    # return the result
    return None

# enter the operation in line below in the polar format
polar_calculator((385,34.5) + (348.9,-94) + (316.3,158.9))
