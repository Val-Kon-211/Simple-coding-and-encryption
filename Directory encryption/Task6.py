import os

def form_dict():
    d = {}
    iter = 0
    for i in range(0,127):
        d[iter] = chr(i)
        iter = iter +1
    return d

def encode_val(word):
    list_code = []
    lent = len(word)
    d = form_dict() 

    for w in range(lent):
        for value in d:
            if word[w] == d[value]:
               list_code.append(value) 
    return list_code

def comparator(value, key):
    len_key = len(key)
    dic = {}
    iter = 0
    full = 0

    for i in value:
        dic[full] = [i,key[iter]]
        full = full + 1
        iter = iter +1
        if (iter >= len_key):
            iter = 0 
    return dic 

def full_encode(value, key):
    dic = comparator(value, key)
    lis = []
    d = form_dict()

    for v in dic:
        go = (dic[v][0]+dic[v][1]) % len(d)
        lis.append(go) 
    return lis

def decode_val(list_in):
    list_code = []
    lent = len(list_in)
    d = form_dict() 

    for i in range(lent):
        for value in d:
            if list_in[i] == value:
               list_code.append(d[value]) 
    return list_code

def full_decode(value, key):
    dic = comparator(value, key)
    d = form_dict() 
    lis =[]

    for v in dic:
        go = (dic[v][0]-dic[v][1]+len(d)) % len(d)
        lis.append(go) 
    return lis

def cipher_directory(path, key):
    for root, dirs, files in os.walk(path):
        for file in files:
            file_path = os.path.join(root,file)
            with open(file_path, 'r') as f:
                text = f.read()
                
                key_encoded = encode_val(key)
                value_encoded = encode_val(text)
                
                shifre = full_encode(value_encoded, key_encoded)
                
                text_shifre = ''.join(decode_val(shifre))
            
            new_file = open(r"C:\Users\konva\Documents\STUDY\Information Security\Task6\shifre_dir.txt", "a")
            new_file.write(file_path + '\n' + text_shifre +'\n')
            new_file.close()
            
    for root, dirs, files in os.walk(path, topdown=False):
        for name in files:
            os.remove(os.path.join(root, name))
        for name in dirs:
            os.rmdir(os.path.join(root, name))
    os.rmdir(path)
                
def decode_directory(file_path, k):
    
    with open(file_path, "r") as f:
        path = f.readline()[:-1]
        shifre = f.readline()[:-1]
        
        while path != '': 
            key = encode_val(k)
            decoded = full_decode(encode_val(shifre), key)
            decode_word_list = decode_val(decoded)
            result = ''.join(decode_word_list)
            
            el_path = path.split('\\')
            dir = '\\'.join(el_path[:-1])
            file = el_path[-1]
            
            if os.path.isdir(dir) == False:
                os.mkdir(dir)
                
            with open(path, "w") as nf:
                nf.write(result)
            
            path = f.readline()[:-1]
            shifre = f.readline()[:-1]
    
    os.remove(file_path)

path = r"C:\Users\konva\Documents\STUDY\Information Security\Task6\files"
file_path = r"C:\Users\konva\Documents\STUDY\Information Security\Task6\shifre_dir.txt"

#cipher_directory(path, 'key')
decode_directory(file_path, 'key')