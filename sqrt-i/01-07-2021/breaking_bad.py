import json
import zipfile
import hashlib
import zipHandle

jsonFile = open("01-07-2021/breaking_bad_char.json")

data = json.load(jsonFile)

charactersList = []
md5List = []

for i in data:
    charactersList.append(i["name"]+"__"+i["nickname"])

for character in charactersList:
    objHash = hashlib.md5(character.encode("utf-8"))
    md5List.append(objHash.hexdigest())

md5CharDic = {}

for i in range(0,len(md5List)):
    md5CharDic[md5List[i]] = charactersList[i]

zipHandle.recursivelyExtract("01-07-2021/zipFiles/3ec9085f6b33c86fbccd2d191c0542b2.zip",md5CharDic)