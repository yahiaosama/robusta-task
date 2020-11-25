from .exceptions.unknowntype_error import UnknownTypeError
class Cipher:
    def __init__(self, given_string):
        if(type(given_string) != str):
            raise UnknownTypeError(given_string, "Expected input to be of type str instead input of type" + type(given_string).__name__ + " is given")

        self.given_string = given_string

