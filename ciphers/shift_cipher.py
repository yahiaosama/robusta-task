from .cipher import Cipher

class ShiftCipher(Cipher):
    def __init__(self, given_string):
        super().__init__(given_string)
        self.alphabet_letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

    def encrypt(self) -> str:
        result = str()
        for char in self.given_string:
            if char == ' ' or char == ',':
                result += char
            else:
                encrypted_char_index = (self.alphabet_letters.index(char) + 3) % len(self.alphabet_letters)
                result += self.alphabet_letters[encrypted_char_index]
        return result

    def decrypt(self) -> str:
        result = str()
        for char in self.given_string:
            if char == ' ' or char == ',':
                result += char
            else:
                decrypted_char_index = self.alphabet_letters.index(char) - 3
                if decrypted_char_index < 0:
                    decrypted_char_index = len(self.alphabet_letters) - decrypted_char_index
                result += self.alphabet_letters[decrypted_char_index]
        return result

