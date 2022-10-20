# Шифр Цезаря
# При шифровании каждый символ заменяется другим,
# отстоящим от него в алфавите на фиксированное число позиций.
# code_number = 3

alfabet_eng = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
alfabet_rus = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'

string1 = 'hello, дивный новый мир!'


def encode(string, code_number):
    encoded_string = ""
    for i in string:
        if i in alfabet_rus:
            encoded_string = encoded_string + alfabet_rus[int(alfabet_rus.index(i)) + code_number]
        elif i in alfabet_eng:
            encoded_string = encoded_string + alfabet_eng[int(alfabet_eng.index(i)) + code_number]
        else:
            encoded_string += i
    return encoded_string


encoded_string1 = encode(string1, 3)


def decode(string, code_number):
    decoded_string = ""
    for i in string:
        if i in alfabet_rus:
            decoded_string = decoded_string + alfabet_rus[int(alfabet_rus.index(i)) - code_number]
        elif i in alfabet_eng:
            decoded_string = decoded_string + alfabet_eng[int(alfabet_eng.index(i)) - code_number]
        else:
            decoded_string += i
    return decoded_string


decoded_string1 = decode(encoded_string1, 3)

print('original string: ', string1)
print('string after encoding: ', encoded_string1)
print("string after decoding: ", decoded_string1)
