def adjusted_key(text,key):
    text = text
    text = text.replace(" ","")
    text = text.replace("!","")
    text = text.replace(".","")
    text = text.replace(",","")
    text = text.replace("-","")

    adj_key = ""
    klen = len(key)
    tlen = len(text)
    ajlen = len(adj_key)


    iteration = 0
    extra = 0
    count = 0
    rep = 0
    extracount = 0
    lcount = 0
    
    while(ajlen<tlen):
        iteration = tlen//klen
        extra = tlen % klen 
        if (extra==0):
            while(count<iteration):
                adj_key = adj_key + key
                count = count + 1
        else:
            while (rep<iteration):
                adj_key = adj_key + key
                rep = rep + 1
            while (extracount < extra):
                adj_key = adj_key + key[lcount]
                extracount = extracount + 1
                lcount = lcount + 1
        ajlen = len(adj_key)  
    return adj_key


   

def encrypt_vigenere():
    in_file = input("What is the name of the file you would like to encode: ")
    in_file = open(in_file)
    text = in_file.readline()
    in_file.close()
    text = text.lower()
    key = input("Please enter a key value: ")
    key = key.lower()
    adj_key = adjusted_key(text,key)

    ntext = text
    text = text

    indexwithnoletter = []
    stringatindex = []
    newval = 0
    k = 0

    klen = len(key)
    tlen = len(text)
    ajlen = len(adj_key)

    while (k<tlen):
        ntextkey = ntext[k]
        istrue = ntextkey.isalpha()
        if(istrue == False):
            indexwithnoletter.append(k)
            stringatindex.append(ntextkey)
        k+=1


    text = text.replace(" ","")
    text = text.replace("!","")
    text = text.replace(".","")
    text = text.replace(",","")
    text = text.replace("-","")

    tlen = len(text)

    encrypted_text = ""
    i = 0
    j = 0

    a = ""
    b = 0

    c = ""
    d = 0

    l = 0
    
    ajlen = len(adj_key)


    while (ajlen>i):
        a = adj_key[i]
        b = ord(a)
        c = text[i]
        d = ord(c)
        if (64<b<91):
            b = b - 65
            l = 65
        elif (96<b<123):
            b = b - 97
            l = 97
        
        d = d - 97
        
        newval = b + d
        if (newval>26):
            newval = newval%26
        
        newval = newval + l
        z =chr(newval)
        encrypted_text = encrypted_text + z
        i+=1
    num_set = len(indexwithnoletter)
    string_set = len(stringatindex)
    q = 0
    if (num_set == string_set):
        while (q<num_set):
            s = indexwithnoletter[q]
            u = stringatindex[q]
            encrypted_text = encrypted_text[:s] + u + encrypted_text[s:]
            q+=1
    l_file = input("what is the name of the file you would like to print the encoding in: ")
    l_file = open(l_file, 'a')
    encrypted_text = l_file.write(encrypted_text)
    l_file.close()
    print('DONE!')




def decrypt_vigenere():
    in_file = input("What is the name of the file you would like to decode: ")
    in_file = open(in_file)
    text = in_file.readline()
    in_file.close()
    text = text.lower()
    key = input("What is the decryption key: ")
    key = key.lower()
    ntext = text
    text = text 
    adj_key = adjusted_key(text,key)
    ajlen = len(adj_key)
    
    indexwithnoletter = []
    stringatindex = []
    newval = 0
    k = 0

    tlen = len(text)
    ajlen = len(adj_key)
    while (k<tlen):
        ntextkey = ntext[k]
        istrue = ntextkey.isalpha()
        if(istrue == False):
            indexwithnoletter.append(k)
            stringatindex.append(ntextkey)
        k+=1

    text = text.replace(" ", "")

    i = 0
    l = 0
    decrypted_text = ""
    while (ajlen>i):
        a = adj_key[i]
        b = ord(a)
        c = text[i]
        d = ord(c)
        if (97<=b<=122):
            l = 97
        elif (65<=b<=80):
            l = 65
        newval = d-b
        newval = newval + 26
        newval = newval%26
        newval = newval + 97
        z = chr(newval)
        decrypted_text = decrypted_text + z
        i+=1
    num_set = len(indexwithnoletter)
    string_set = len(stringatindex)
    q = 0
    if (num_set == string_set):
        while (q<num_set):
            s = indexwithnoletter[q]
            u = stringatindex[q]
            decrypted_text = decrypted_text[:s] + u + decrypted_text[s:]
            q+=1
    f_name = input("What is the name of the file you would like to store you decryption in: ")
    f_name = open(f_name, 'a')
    decrypted_text = f_name.write(decrypted_text)
    f_name.close()
    print('DONE!')

def menu():
    choice = 0
    print("1.) Encrypt")
    print("2.) Decrypt")
    print("3.) Quit")
    choice = int(input("What would you like to do: "))
        
    if (choice == 1):
        print('Encrypting Text.................')
        encrypt_vigenere()
    elif (choice == 2):
        print('Decrypting Text.................')
        decrypt_vigenere()
    elif(choice == 3):
        exit()
    else:
        while(choice!=1 and choice != 2 and choice != 3):
            print("1.) Encrypt")
            print("2.) Decrypt")
            print("3.) Quit")
            choice = int(input("Choose an option number: "))
               
        if (choice == 1):
            print('Encrypting Text.................')
            encrypt_vigenere()
        elif (choice == 2):
            print('Decrypting Text.................')
            decrypt_vigenere()
        elif(choice == 3):
            System.out.println("You are not quiting the program")
            exit()
            
menu()