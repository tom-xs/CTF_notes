from zipfile import ZipFile as zp
import zipfile

def checkZipInfo(path_to_zip):
    with zp(path_to_zip,"r") as zipObj:
        return zipObj.infolist()

def extract(path_to_zip,pswd):
    with zp(path_to_zip,"r") as zipObj:
        zipObj.extractall("01-07-2021/zipFiles",pwd=pswd.encode())

def recursivelyExtract(path_to_zip,pswdDic):
    try:
        infoList = checkZipInfo(path_to_zip)
        filename = infoList[0].filename
        extract(path_to_zip,pswdDic[path_to_zip.split("/")[-1][:-4]])
        recursivelyExtract("01-07-2021/zipFiles/"+filename,pswdDic)
    except zipfile.BadZipFile:
        print("flag encontrada")
