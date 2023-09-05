from morse import Morse

if __name__ == '__main__':
    morse = Morse()
    encoded = morse.encode(input('Write a text: '))
    print('Morse: ', encoded)
    print('Decode: ', morse.decode(encoded))
