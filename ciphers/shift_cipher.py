from .cipher import Cipher

class ShiftCipher(Cipher):
    def __init__(self, given_string):
        super().__init__(given_string)

    def encrypt(self) -> str:
        result = str()
        for char in self.given_string:
            if char == ' ' or char == ',':
                result += char
            else:
                char_ascii = ord(char)
                encrypted_char_ascii = char_ascii + 3
                result += chr(encrypted_char_ascii)
        return result

    def decrypt(self) -> str:
        result = str()
        for char in self.given_string:
            if char == ' ' or char == ',':
                result += char
            else:
                char_ascii = ord(char)
                decrypted_char_ascii = char_ascii - 3
                result += chr(decrypted_char_ascii)
        return result

