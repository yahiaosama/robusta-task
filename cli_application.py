import click
from ciphers.shift_cipher import ShiftCipher
from ciphers.reverse_cipher import ReverseCipher
from ciphers.matrix_cipher import MatrixCipher
from ciphers.exceptions.unknowntype_error import UnknownTypeError

@click.command()
@click.option('--string', prompt='String to be encrypted or decrypted', help="String to be encrypted or decrypted")
@click.option('--decryption_matrix', prompt='Matrix to be decrypted only works with matrix cipher', multiple=True, help="Matrix to be decrypted only works with matrix cipher decryption")
@click.option('--algorithm-name', prompt='Algorithm name to be used', type=click.Choice(['Shift', 'Matrix', 'Reverse'], case_sensitive=False), help='The name of the algorithm to be used to perform the desired cipher operation with')
@click.option('--method', prompt='Method to be used', type=click.Choice(['Encrypt', 'Decrypt'], case_sensitive=False), help='The name of the method to be performed using the desired cipher algorithm')

def main(string, decryption_matrix, algorithm_name, method):
    cipher = None
    result = str()
    if algorithm_name.lower() == 'shift':
        try:
            cipher = ShiftCipher(string)
        except UnknownTypeError as e:
            click.echo(e.message)
            main()
    elif algorithm_name.lower() == 'reverse':
        cipher = ReverseCipher(string)
    else:
        if method.lower() == 'decrypt':
            try:
                processed_matrix = process_decryption_matrix(decryption_matrix)
                cipher = MatrixCipher(matrix_to_decrypt=processed_matrix)
            except UnknownTypeError as e:
                click.echo(e.message)
                main()
        else:
            try:
                cipher = MatrixCipher(given_string=string)
            except UnknownTypeError as e:
                click.echo(e.message)
                main()

    if method.lower() == 'encrypt':
        result = cipher.encrypt()
        if type(result) == list:
            result = lists_to_string(result)
    else:
        result = cipher.decrypt()
    
    click.echo('The ' + method.lower() + 'ed result is: ' + result)

def process_decryption_matrix(decryption_matrix):
    result = []
    matrix_entries = ''.join(decryption_matrix)
    splitted_matrix_entries = matrix_entries.split(' ')
    filtered_matrix_entries = [number for number in splitted_matrix_entries if number.isnumeric()]
    entries_count = 0
    char_values = []
    for entry_index, entry in enumerate(filtered_matrix_entries):
        char_values.append(int(entry))
        if (entry_index + 1) % 16 == 0:
            result.append(char_values)
            char_values = []
    return result

def lists_to_string(input_lists):
    result = str()
    for input_list in input_lists:
        for number in input_list:
            result += str(number) + ' '
        result += '\n'
    return result

if __name__ == '__main__':
    main()
