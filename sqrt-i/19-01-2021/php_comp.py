import hashlib

def funcaofoda(s):
    r1 = 0
    r2 = 999999999
    for i in range(r1,r2):
        s_foda = s+str(i)
        hash_foda = hashlib.md5(s_foda.encode("utf-8")).hexdigest()
        if(hash_foda[0:2] == s_foda[0:2] and hash_foda[2:].isdigit()):
            print(s_foda + " | "+hash_foda)

s = "0e"

funcaofoda(s)