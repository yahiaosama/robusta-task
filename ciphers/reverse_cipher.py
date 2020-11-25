import requests
from .cipher import Cipher

class ReverseCipher(Cipher):
    def __init__(self, given_string):
        super().__init__(given_string)
        self.encryption_endpoint = 'http://backendtask.robustastudio.com/encode'
        self.decryption_endpoint = 'http://backendtask.robustastudio.com/decode'

    def encrypt(self) -> str:
        result = requests.post(self.encryption_endpoint, data={'string':self.given_string})
        return result.json()['string']

    def decrypt(self) -> str:
        result = requests.post(self.decryption_endpoint, data={'string':self.given_string})
        return result.json()['string']

