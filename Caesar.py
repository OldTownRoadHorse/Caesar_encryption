old = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
stepen = int(3)


def cip():
    cipher = input("Message for encryption:  ").upper()
    itog = ''
    for i in cipher:
        mesto = old.find(i)
        new_mesto = mesto + stepen
        if i in old:
            itog += old[new_mesto]
        else:
            itog += i
    print(itog)
    
def ucip():
    ucipher = input("Message for decoding:  ").upper()
    itog = ''
    for i in ucipher:
        mesto = old.find(i)
        new_mesto = mesto - stepen
        if i in old:
            itog += old[new_mesto]
        else:
            itog += i
    print (itog)

while True:
    chagag = input("Encryption[1]:  \nDecoding[2]:  ")

    itog = ''

    if chagag == "1":
        cip()
    
    elif chagag == "2":
        ucip()