from langchain.tools import tool
# from rich import print
import secrets,string


@tool
def password_generator(length:int)->str:
    """
Generate a secure random password.

Accepts the desired password length.

Returns a password containing letters,

numbers and special characters.    """
    
    if length<=0:
        return f"Desired Password Lenght is invalid."

    small_alphabet = (string.ascii_lowercase)
    capital_alphabet = (string.ascii_uppercase)
    digit = (string.digits)
    punctuation = (string.punctuation)

    combined_list = small_alphabet+capital_alphabet+digit+punctuation

    password =""
    for i in range(length):
        char = secrets.choice(combined_list)
        password+= char
    return password

