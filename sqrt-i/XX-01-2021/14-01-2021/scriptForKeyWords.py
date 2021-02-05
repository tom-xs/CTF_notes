lista = []

with open("sqrt-i\\14-01-2021\\CeWL\\palavraschave.txt","r") as file:
    for line in file:
        lista.append(line[:-1])

with open("sqrt-i\\14-01-2021\\textfile.txt","w") as file:
    for i in lista:
        file.write(i+"surgeon"+"\n")
