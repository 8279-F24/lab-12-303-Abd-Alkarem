import time
from adafruit_circuitplayground import cp

MORSE_CODE = {
    'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.',
    'f': '..-.', 'g': '--.', 'h': '....', 'i': '..', 'j': '.---',
    'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---',
    'p': '.--.', 'q': '--.-', 'r': '.-.', 's': '...', 't': '-',
    'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-', 'y': '-.--',
    'z': '--..', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    '0': '-----',
}

def clean_sentence(sentence):
    return ''.join(char for char in sentence.lower() if char in MORSE_CODE or char == ' ')

def sentence_to_morse(sentence):
    morse_list = []
    for word in sentence.split(' '):
        for char in word:
            if char in MORSE_CODE:
                morse_list.append(MORSE_CODE[char])
        morse_list.append(' ')
    return morse_list[:-1]

def display_morse_on_leds(morse_list, unit_length):
    cp.pixels.brightness = 0.2
    cp.pixels.fill((0, 0, 0))
    for symbol in morse_list:
        if symbol == '.':
            cp.pixels.fill((0, 255, 0))
            time.sleep(unit_length)
        elif symbol == '-':
            cp.pixels.fill((0, 0, 255))
            time.sleep(unit_length * 3)
        elif symbol == ' ':
            cp.pixels.fill((0, 0, 0))
            time.sleep(unit_length * 7)
        cp.pixels.fill((0, 0, 0))
        time.sleep(unit_length)

unit_length = float(input("Enter unit length (0 to 1 seconds): "))
sentence = input("Enter a sentence: ")
clean_input = clean_sentence(sentence)
morse_code_list = sentence_to_morse(clean_input)
print("Morse Code List:", morse_code_list)
display_morse_on_leds(morse_code_list, unit_length)
