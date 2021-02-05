input = input("Flag: ")
num = 7
middlepart = ""
#esse primeiro "for" subtrai 8 do char de cada char no input 
for n in input:
	n = ord(n)
	n += 2
	n -= 10
	n = chr(n)
	middlepart += n
	
jars = []
#adiciona 7 strings vazias a "jars"
for n in range(num):
	jars.append("")
jarnum = 0

#divide a string "middlepart" em 6 de forma que vai adicinando elementos entre posições alternadamente (com exceção do primeiro termo)
#ex: middle = "123456789" -> jars = ["1","27","38","49","5","6"]
for n in middlepart:
	jars[jarnum] +=n
	if jarnum == 6:
		jarnum = 0
	jarnum += 1
result = ""

#concatena o "jars" em uma string
for n in range(7):
	result += jars[n]
output = ""

#soma o valor de cada char no "result" em 5
for n in result:
	n = ord(n)
	n += 5
	n = chr(n)
	output += n
print(output)


	
