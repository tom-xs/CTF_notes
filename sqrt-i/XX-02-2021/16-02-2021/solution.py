s = {'character': 'pf{', 'index': 1}, {'character': 'tic', 'index': 0}, {'character': 'lk1', 'index': 4}, {'character': '}lz', 'index': 5}, {'character': 'hyt', 'index': 2}, {'character': 's0n', 'index': 3}
new_dic = {}
r = ""
for i in s:
    new_dic[i['index']] = i['character']

for i in range(len(new_dic)):
    n = new_dic[i][1:]
    n2 = new_dic[i][0]
    n = n+n2
    r = r + n

print(r)
