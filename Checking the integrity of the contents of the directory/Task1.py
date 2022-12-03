import os
import sys

def get_files_hash_sum(path):
    files_hash_sum = {}
    for root, dirs, files in os.walk(path):
        for file in files:
            with open(os.path.join(root,file), 'rb') as f:

                # считываем текст и переводим его в последовательность битов
                text = f.read()
                bits = str(bin(int.from_bytes(text, sys.byteorder))[2:])
                
                # берём первые 16 бит
                b = bits[:16]
                if len(b) < 16:                 # если длина меньше 16
                    b = b + '0'*(16-len(b))     # в конец добавляем нули
                
                hash_sum = b                    # присваиваем первые 16 бит файла хэш-сумме
                bits = bits[16:]                # "отрезаем" их от битовой посл-ти
                
                while len(bits) > 0:            # пока не пройдёмся по всему файлу
                    b = bits[:16]               # определяем следующие 16 бит
                    
                    if len(b) < 16:
                        b = b + '0'*(16-len(b))
                    bits = bits[16:]
                    
                    # считаем хэш-сумму
                    hash_sum = str(bin(int(hash_sum, 2) ^ int(b, 2))[2:])
                    if len(hash_sum) < 16:                                  # если длина хэш-суммы меньше 16
                        hash_sum = '0'*(16-len(hash_sum)) + hash_sum        # добавляем ведущие 0
                # добавляем хэш-сумму в список
                files_hash_sum[os.path.join(root,file)] = hash_sum
    return files_hash_sum

path = r"C:\Users\konva\Documents\STUDY\Information Security\Task1\files"

# запись хэш-суммы файлов в файл
#fhs1 = get_files_hash_sum(path)
          
#fp = open(r"C:\Users\konva\Documents\STUDY\Information Security\Task1\file_hash.txt", "w")
'''for el in fhs1:
    fp.write(el + ': ' + fhs1[el]+'\n')
fp.close()'''

# загрузка файла с хэш-суммами
check_file = open(r"C:\Users\konva\Documents\STUDY\Information Security\Task1\file_hash.txt", "r")
check_fhs = {}
# считываем строки из файла
while True:
    # считываем строку
    l = check_file.readline()
    # прерываем цикл, если строка пустая
    if not l:
        break
    line = l.strip()
    ind = line.find(':', 2)
    file_path = line[:ind]
    file_hash_sum = line[ind+2:]
    check_fhs[file_path] = file_hash_sum

check_file.close()

fhs2 = get_files_hash_sum(path)
flag = False
for elem in fhs2:
    if fhs2[elem] != check_fhs[elem]:
        flag = True
        print('Файл', elem, 'был изменён')

if not flag:
    print('Ни один файл в дериктории не был изменён')