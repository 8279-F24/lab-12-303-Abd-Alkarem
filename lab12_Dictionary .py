MORSE_CODE = {
    'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.', 'f': '..-.',
    'g': '--.', 'h': '....', 'i': '..', 'j': '.---', 'k': '-.-', 'l': '.-..',
    'm': '--', 'n': '-.', 'o': '---', 'p': '.--.', 'q': '--.-', 'r': '.-.',
    's': '...', 't': '-', 'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-',
    'y': '-.--', 'z': '--..', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',
    '9': '----.', '0': '-----'
}

def clean_sentence(sentence):
    return ''.join(char.lower() for char in sentence if char.lower() in MORSE_CODE or char == ' ')

def sentence_to_morse(sentence):
    morse_list = []
    for word in sentence.split(' '):
        for char in word:
            if char in MORSE_CODE:
                morse_list.append(MORSE_CODE[char])
        morse_list.append(' ')
    return morse_list[:-1]

def create_timed_morse_list(morse_list):
    timed_list = []
    for symbol in morse_list:
        if symbol == ' ':
            timed_list.append(' ')
        else:
            for part in symbol:
                timed_list.append(part)
                timed_list.append('1')
            timed_list.pop()
            timed_list.append('3')
    timed_list.pop()
    return timed_list

def main():
    sentence = input("Enter a sentence: ")
    clean_input = clean_sentence(sentence)
    morse_code_list = sentence_to_morse(clean_input)
    timed_morse_list = create_timed_morse_list(morse_code_list)
    print("Morse Code List:", morse_code_list)
    print("Timed Morse Code List:", timed_morse_list)

if __name__ == "__main__":
    main()
