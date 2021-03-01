a = "A, C, G, K, M, R, T, U".split(", ")
n = 8**len(a)
flag = ".flag ictf{"+str(n)+"_"

for i in range(n):
    if(i == 250-1):
        s = oct(i)
        s = list(str(s)[2:].zfill(8))
        for j in range(8):
            flag+= a[int(s[j])]
        break

print(flag+"}")