"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""


#TODO: define your EXPECTED_BAKE_TIME (required) and PREPARATION_TIME (optional) constants below.
EXPECTED_BAKE_TIME = 40
PREPERATION_TIME = 10

#TODO: Remove 'pass' and complete the 'bake_time_remaining()' function below.
def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """

    time_remaining = EXPECTED_BAKE_TIME - elapsed_bake_time
    return time_remaining


#TODO: Define the 'preparation_time_in_minutes()' function below.
# To avoid the use of magic numbers (see: https://en.wikipedia.org/wiki/Magic_number_(programming)), you should define a PREPARATION_TIME constant.
# You can do that on the line below the 'EXPECTED_BAKE_TIME' constant.
# This will make it easier to do calculations, and make changes to your code.



def preparation_time_in_minutes(number_of_layers):
    """Define the preparation_time_in_minutes() function that takes the number_of_layers you want to add to the lasagna as an argument and returns how many minutes you would spend making them.
    Assume each layer takes 2 minutes to prepare."""
    prep_time = (number_of_layers * 2)
    return prep_time

#TODO: define the 'elapsed_time_in_minutes()' function below.
def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    '''Define the elapsed_time_in_minutes() function that takes two parameters as arguments:

    number_of_layers (the number of layers added to the lasagna)
    elapsed_bake_time (the number of minutes the lasagna has spent baking in the oven already).
    This function should return the total minutes you have been in the kitchen cooking — your preparation time layering + the time the lasagna has spent baking in the oven.'''
    elapsed_time = (number_of_layers * 2) + elapsed_bake_time
    return elapsed_time



# TODO: Remember to go back and add docstrings to all your functions
#  (you can copy and then alter the one from bake_time_remaining.)
