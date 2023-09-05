class Morse:
    MORSE_CODE_DICT = {'A': '.-', 'B': '-...',
                       'C': '-.-.', 'D': '-..', 'E': '.',
                       'F': '..-.', 'G': '--.', 'H': '....',
                       'I': '..', 'J': '.---', 'K': '-.-',
                       'L': '.-..', 'M': '--', 'N': '-.',
                       'O': '---', 'P': '.--.', 'Q': '--.-',
                       'R': '.-.', 'S': '...', 'T': '-',
                       'U': '..-', 'V': '...-', 'W': '.--',
                       'X': '-..-', 'Y': '-.--', 'Z': '--..',
                       '1': '.----', '2': '..---', '3': '...--',
                       '4': '....-', '5': '.....', '6': '-....',
                       '7': '--...', '8': '---..', '9': '----.',
                       '0': '-----', ', ': '--..--', '.': '.-.-.-',
                       '?': '..--..', '/': '-..-.', '-': '-....-',
                       '(': '-.--.', ')': '-.--.-', '!': '-.-.--'}

    @staticmethod
    def encode(text):
        result = ''
        for char in text:
            if char == ' ':
                result += '/ '
            else:
                result += Morse.MORSE_CODE_DICT.get(char.upper(), '') + ' '
        return result.rstrip()

    @staticmethod
    def decode(encoded_text):
        result = ''
        for letter in encoded_text.split(' '):
            if letter == '/':
                result += ' '
            else:
                result += Morse.inverted_morse_code_dict().get(letter, '')
        return result

    @staticmethod
    def inverted_morse_code_dict():
        return {v: k for k, v in Morse.MORSE_CODE_DICT.items()}

