import os
import sys

analogue_ru_eng = {'а': 'a', 'е': 'e', 'о': 'o', 'р': 'p',
                   'с': 'c', 'у': 'y', 'х': 'x', 'А': 'A',
                   'В': 'B', 'Е': 'E', 'К': 'K', 'О': 'O',
                   'Р': 'P', 'С': 'C', 'Т': 'T', 'Х': 'X'}

analogue_eng_ru = {'a': 'а', 'e': 'е', 'o': 'о', 'p': 'р',
                   'c': 'с', 'y': 'у', 'x': 'х', 'A': 'А',
                   'B': 'В', 'E': 'Е', 'K': 'К', 'O': 'О',
                   'P': 'Р', 'C': 'С', 'T': 'Т', 'X': 'Х'}

mes_path = r"C:\Users\konva\Documents\STUDY\Information Security\Task4\Text.txt"
cont_path = r"C:\Users\konva\Documents\STUDY\Information Security\Task4\Container.txt"


def coding(mes_path, cont_path):
    mess = open(mes_path, 'rb')
    text_mes = mess.read().decode('utf-8').encode('cp1251')
    bits = ''.join(f'{x:08b}' for x in text_mes)
    mess.close()

    # считываем текст из контейнера
    container = open(cont_path, "r", encoding='utf-8')
    text = container.read()
    container.close()
    
    # индекс последней считанной буквы-аналога
    ind = 0
    
    # прячем сообщение
    for bit in bits:
        for i in range(ind, len(text)):
            if text[i] in analogue_ru_eng.keys():
                if bit == '1':
                    text = text[:i] + analogue_ru_eng[text[i]] + text[i+1:]
                ind = i+1
                break
    
    container = open(cont_path, "w", encoding='utf-8')
    container.write(text)
    container.close()

#-------------------------------------------------------------

def decoding(cont_path):
    # считываем текст из контейнера
    container = open(cont_path, "r", encoding='utf-8')
    text = container.read()
    container.close()
    
    bits = ''
    
    for i in text:
        if i in analogue_ru_eng.keys():
            bits += '0'
        elif i in analogue_eng_ru.keys():
            bits += '1'
    
    mes = ''
    letter_b = '1'
    
    while int(letter_b, 2) != 0:
        letter_b = bits[:8]
        if int(letter_b, 2) != 0:
            letter = int(letter_b, 2).to_bytes(1, byteorder='big')
            mes += letter.decode('cp1251')
            bits = bits[8:]
    
    with open(r"C:\Users\konva\Documents\STUDY\Information Security\Task4\Text_res.txt", "w") as f:
        f.write(mes)
        f.close()
        

#coding(mes_path, cont_path)
decoding(cont_path)