"""
Created by: Dat Nguyen
Created on: Feb 2026
This module will show the area and perimeter of a rectangle on the micro:bit.
"""

from microbit import *

display.scroll("A rectangle has dimensions 5 cm & 3 cm.")
display.scroll("The perimeter would be: " + str(2 * (5 + 3)) + " cm.")
display.scroll("The area would be: " + str(5 * 3) + " cm^2.")
