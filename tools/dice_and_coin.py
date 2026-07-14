from langchain.tools import tool
from random import randint,choice
@tool
def dice(number_of_face:int):
    """
    Returns the number that came after rolling the dice

    It can have any number_of_face as provided in the input and can roll accordinglt
    """

    if number_of_face<=0:
        return f"Invalid number of faces."

    num = randint(1,number_of_face)
    return num

@tool
def coin():
    """
    Return either head or tail when a coin is tossed.
    """

    output = ['Heads','Tails']

    return choice(output)

