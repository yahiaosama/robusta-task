from .cipher import Cipher
from .matrix_based_cipher import MatrixBasedCipher
from .constants import encryption_matrix, decryption_matrix

class MatrixCipher(MatrixBasedCipher):
    def __init__(self, given_string="", matrix_to_decrypt=[[]]):
        super().__init__(given_string, matrix_to_decrypt)
        self.encryption_matrix = encryption_matrix
        self.decryption_matrix = decryption_matrix

    def encrypt(self) -> str:
        result = str()
        matrix_multiplication_result = []
        given_string_binary_values = []
        for char in self.given_string:
            binary_ascii_value = self.char_to_16bit_binary(char)
            given_string_binary_values.append(binary_ascii_value)

        return self.multiply_matrices(self.encryption_matrix, given_string_binary_values)


    def decrypt(self) -> str:
        result = str()
        resulted_matrix = self.multiply_matrices(self.decryption_matrix, self.matrix_to_decrypt)
        rounded_binary_lists = self.round_floats(resulted_matrix)
        return self.convert_binary_to_chars(rounded_binary_lists)


    def multiply_matrices(self, first_matrix, second_matrix):
        resulted_matrix = []
        for single_column in second_matrix:
            row_by_column_product = []
            for row in first_matrix:
                product_sum = 0
                for column_number, number in enumerate(row):
                    product_sum += number * float(single_column[column_number])
                row_by_column_product.append(product_sum)
            resulted_matrix.append(row_by_column_product)
        return resulted_matrix



    def char_to_16bit_binary(self, char):
        ascii_value = ord(char)
        binary_value = bin(ascii_value)
        padded_binary_value = binary_value[2:].zfill(16)
        return padded_binary_value

    def round_floats(self, floats_lists):
        result = []
        for floats_list in floats_lists:
            result_floats_list = []
            for single_float in floats_list:
                integer_float = int(round(single_float))
                if integer_float != 0:
                    result_floats_list.append(1)
                else:
                    result_floats_list.append(0)
            result.append(result_floats_list)
        return result

    def convert_binary_to_chars(self, rounded_binary_lists):
        decrypted_string = str()
        for rounded_binary_list in rounded_binary_lists:
            rounded_binary_string = ''.join([str(rounded_binary_value) for rounded_binary_value in rounded_binary_list])
            char_ascii_value = int(rounded_binary_string, 2)
            decrypted_string += chr(char_ascii_value)
        return decrypted_string
