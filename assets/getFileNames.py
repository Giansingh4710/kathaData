#for giani sher singh ji SGGSJI Katha

import os
import pyperclip

pathToAudios="./Kathas/AdiMaharaj/"

def makeIntoNewName(name):
    newName=""
    for char in name:
        if(ord(char)>1000):
            # print(char+": ",end="")
            # print(ord(char))
            newName+="1"
        else:
            newName+=char
    return newName

def printForJs():
    theList=os.listdir(pathToAudios)
    print("const audios=[")
    for i in theList:
        print("{",end="")
        print(f"'title':",end="")
        print(f"'{i}',",end="")
        print(f"'href': ",end="")
        print(f"'{makeIntoNewName(i)}'",end="")
        print("},")
    print("]")

def renameForZip():
    theList=os.listdir(pathToAudios)
    for file in theList:
        newName=""
        for char in file:
            if(ord(char)>1000):
                # print(char+": ",end="")
                # print(ord(char))
                newName+="1"
            else:
                newName+=char
        # print(pathToAudios+file,pathToAudios+newName)
        os.rename(pathToAudios+file,pathToAudios+newName)


#First run this func to print to copy names to js. 
# printForJs()

# then run this fun to rename so they can be zipped
# renameForZip()

#-----------------------------------------------------------------------------------------------

#for santhiya pothi
def printForJsSanthiya():
    pdfPath="./pdfs/"
    theList=os.listdir(pdfPath)
    # theList=[pdfPath+i+"/" for i in theList]
    returnLst=[]
    for folder in theList:
        d={"folderName":folder,"pdfsInFolder":[]}
        folderPath=pdfPath+folder+"/"
        pdfs=os.listdir(folderPath)
        for pdf in pdfs:
            d["pdfsInFolder"].append(pdf)
            # print("{",end="")
            # print(f"'title':",end="")
            # print(f"'{pdf}',",end="")
            # print(f"'href': ",end="")
            # print(f"'{href}'",end="")
            # print("},")
        returnLst.append(d)
    # print(returnLst)
    pyperclip.copy(str(returnLst))


printForJsSanthiya()
