key = ""
with open("sqrt-i\XX-02-2021\\15-02-2021\enc.png",'rb') as arq:
    s = arq.readline(0)
    for i in list(s):
        key = key + '%c'%(ord(i)^)
#.PNG........IHDR
n_size = len(s1)


for i in range(n_size):
    xor = ord(s1[i]) ^ ord(s2[i])
    s = '%c'%xor
    key = key + s

c = 0

print(key.encode("utf-8"))

key_size = len(key)
dic_key = dict(zip((range(key_size)),list(key)))

out = open("sqrt-i\XX-02-2021\\15-02-2021\out","w+b")
with open("sqrt-i\XX-02-2021\\15-02-2021\enc.png",'rb') as arq:
    byte = arq.read(1)
    while(byte!=""):
        if(byte == b''):
            byte = 0 ^ ord(dic_key[c])
        else:
            byte = ord(byte)
            byte = byte ^ ord(dic_key[c])
        out.write(b'%c'%byte)
        byte = arq.read(1)
        c+=1
        if(c == key_size):
            c=0
out.close()