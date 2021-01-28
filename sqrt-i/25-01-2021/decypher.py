def reverse(s):
    p1 = ""
   
    #subtrai 5 de cada in
    for n in s:
        n = ord(n)
        n -=5
        n = chr(n)
        p1+=n
    #print(p1)

    #cria lista vazia l1
    l1 = []
    for i in range(7):
        l1.append("")
    
    #divide o "p1" em lista
    l1[0] = p1[0]
    n = int(len(p1)/6)
    c = 1
    for i in range(1,len(p1[0:]),n):
        l1[c] = p1[i:i+n]
        c+=1

    #reordena "p1" que vira p2
    p2 = ""
    c = 0
    for i in range(len(l1)):
        for j in range(len(l1)):
            try:
                p2+=l1[j][c]
            except:
                pass
        c+=1
    #print(p2)

    #adiciona 8 a cada char
    p3 = ""
    for n in p2:
        n = ord(n)
        n+=8
        n=chr(n)
        p3+=n

    print(p3)
    
reverse("f`k\\0\kmqd-^40ecokhetbx^\..\o`q_kp`z-!od\.")
