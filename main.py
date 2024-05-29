alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

#шифрование
def encrypt(m, k, keyword):
    message = m
    encrypted = ''
    for letter in message:
        if letter in alphabet:
            t = alphabet.find(letter)
            new_key = (t + k) % len(alphabet)
            encrypted += alphabet[new_key]
        else:
            encrypted += letter
    rows = len(encrypted) // len(keyword)
    if len(encrypted) % len(keyword) != 0:
        rows += 1

    indexes = sorted([(index, value) for index, value in enumerate(keyword)], key=lambda item: item[1])
    result = ''

    for row in range(rows):
        for index in indexes:
            position = index[0] * rows + row
            if position < len(encrypted):
                result += encrypted[position]
            else:
                result += ' '
    encrypted = result
    return encrypted


#дешифрование
def decrypt(mess, unlock, keyword):
    rows = len(mess) // len(keyword)
    if len(mess) % len(keyword) != 0:
        rows += 1
    indexes = sorted([(index, value) for index, value in enumerate(keyword)], key=lambda item: item[1])
    indexes = sorted([(index, value) for index, value in enumerate(indexes)], key=lambda item: item[1][0])
    result = ''
    for index in indexes:
       for row in range(rows):
           position = index[0] + len(keyword) * row
           if position < len(mess):
                result += mess[position]
    mess = result

    dencrypted = ' '
    for letter in mess:
        if letter in alphabet:
            t = alphabet.find(letter)
            new_key = (t - unlock) % len(alphabet)
            dencrypted += alphabet[new_key]
        else:
            dencrypted += letter
    return dencrypted

def info():
    print('\nЗашифровать сообщение, нажмите - "1"')
    print('Расшифровать сообщение, нажмите - "2"')
    print('Выйти из программы, нажмите - "0"')

info()
num = int(input())
while num != 0:
    while num != 0 and num != 1 and num != 2:
        print('\nОшибочный ввод. Введите число заново\n')
        number = int(input())
    if num == 1:
        message = input('Введите строку: ').lower()
        key = int(input('Введите ключ: '))
        keyword = input('Введите ключ-слово для 2-го этапа шифрования: ')
        encry = encrypt(message, key, keyword)
        print('Зашифованное сообщение: ', encry)
        info()
        num = int(input())
    elif num == 2:
        dencryptmess = decrypt(encry, key, keyword)
        print('Расшифованное сообщение: ', dencryptmess)
        num = int(input())