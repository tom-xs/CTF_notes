from hashlib import sha256

givenSha = "86515c560fe63bb69f89661e9c6a9a0b5f9a79703af9ddf5eee6e27a117ea1e1"
hashdic = {}

with open("sqrt-i\\14-01-2021\\textfile.txt") as file:
    
    for line in file:
        h = sha256(line[:-1].encode("utf-8")).hexdigest()

        hashdic[h] = line[:-1]


print(".flag ictf{"+hashdic[givenSha]+"}")