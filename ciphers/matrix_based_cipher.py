from .exceptions.unknowntype_error import UnknownTypeError
from .cipher import Cipher

class MatrixBasedCipher(Cipher):
    def __init__(self, given_string, matrix_to_decrypt):
        super().__init__(given_string)
        if matrix_to_decrypt == []:
            raise UnknownTypeError(matrix_to_decrypt, "Expected input matrix for each character to be a 16x1 matrix!. You have entered less than 16 integers")
        if not matrix_to_decrypt == [[]] and not all(len(single_list) == 16 for single_list in matrix_to_decrypt):
            raise UnknownTypeError(matrix_to_decrypt, "Expected input matrix for each character to be a 16x1 matrix! ")

        self.matrix_to_decrypt = matrix_to_decrypt

