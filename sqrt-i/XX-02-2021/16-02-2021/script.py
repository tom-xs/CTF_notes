flag = "<piz1jdjlajdlksajiii>"

#divide a flag em uma lista onde cada coisas tem tamanho 3(co exceção do ultimo, que tem o taamanho que de)
newList = [flag[a:a+3] for a in range(0, len(flag), 3)]

#da um "shift" pra esquerda e cada ellemento da lista
def minus(a_list: list, num: int):
    a_values = []
    for the_list in a_list[num]:
        for real_list in the_list:
            for string in real_list:
                a_values.append(string)
    b_values = []
    count = 0 
    for i in a_values:
        b_values.append(a_values[count-1])
        count += 1
    
    return ''.join(b_values)

everything = []
for i in range(len(newList)):
    everything.append(minus(newList,i))

#se na lista tiver algum char contendo "p" "i" "1" "z" "y" ou "s" adiciona os 3 characteres (o elemento da lista naquela
# posição) para places
 
def find(inp_list: list, char_inp: str):
    for character in inp_list:
        if char_inp in character:
            return({"character" : character, "index" : inp_list.index(character)})

places = []
places.append(find(everything,"p"))
places.append(find(everything,"i"))
places.append(find(everything,"1"))
places.append(find(everything,"z"))
places.append(find(everything,"y"))
places.append(find(everything,"s"))



def needed(list_list: list, num: int):
    temp_list = []
    for x in range(len(list_list[0])*num):
        temp_list.append(list_list)
    return(temp_list)

print((needed(places,50000)))
