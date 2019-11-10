morse = {'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.',
         'f': '..-.', 'g': '--.', 'h': '....', 'i': '..', 'j': '.---',
         'k': '-,-', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---',
         'p': '.--.', 'q': '--.-', 'r': '.-.', 's': '...', 't': '-',
         'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-', 'y': '-.--',
         'z': '--..'}


def encode(text):
    text = text.replace(' ', '')
    text = text.lower()
    text = list(text)
    length = len(text)
    i = 0
    morsecode = ''
    while i < length:
        morsecode += morse[text[i]]
        i += 1
    return '\n' + morsecode


def decode(code):
    decoded_text = ''
    refined_code = ''
    key_list = list(morse.keys())
    value_list = list(morse.values())
    coded_list = list(code)
    for element in coded_list:
        index2 = coded_list.index(element)
        for j in value_list:
            if j == element:
                innddex = value_list.index(element)
                decoded_text += key_list[innddex]
                break
            else:
                refined_code += coded_list[index2]
                for k in value_list:
                    if refined_code == k:
                        index3 = value_list.index(refined_code)
                        decoded_text += key_list[index3]
                        continue
    return decoded_text


choice = input('1.Encode\n2.Decode')
if choice == '1':
    input_text = input('enter the text to be encoded : ')
    print(encode(input_text))
if choice == '2':
    code = input('enter code to be decoded : ')
    print(decode(code))

