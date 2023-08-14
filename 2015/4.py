import hashlib  # we need this to generate MD5s

inp = 'ckczppom'    # my input

i = 0
found5 = False                                              # a marker on whether we already found a key with 5 zeros
while True:
    key = inp + str(i)                                      # create the key
    hashed = hashlib.md5(key.encode('utf-8')).hexdigest()   # generate the md5 in hexadecimal
    if hashed[:5] == '00000':                               # if we found a hash starting with 5 zeros
        if not found5:                                      # if we found the first hash starting with 5 zeros print it
            print(i,hashed)
            found5 = True
        if hashed[:6] == '000000':                          # if we found a hash starting with 6 zeros, print it and break
            print(i,hashed)
            break
    i += 1
