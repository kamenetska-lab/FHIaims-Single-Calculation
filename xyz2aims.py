f = open("geometry.in", "w")
mylines = []
mydata = []
titleline = []
linenum=0
startindex = 0
endindex = 0
itemnum = 0
itemnum = 0
with open ("geometry.xyz", "rt") as myfile:
    for myline in myfile:
        mydata.append(myline.rstrip('\n'))
    print(mydata)
    print("hello world")
    for item in mydata:
        str = mydata[itemnum]
        elementa = "26"
        elementb = "6"
        elementc = "1"
        elementd = "79"
        elemente = "44"
        elementf = "7 "
        elementg = "47 "
        elementh = "8 "
        if str.find(elementa, 0, 2) != -1:
            strnew = str + "   Fe"
            strnew = strnew.replace("26","",1)
            mydata[itemnum] = strnew
            print(strnew)
            
        if str.find(elementb, 0, 1) != -1:
            strnew = str + "   C"
            strnew = strnew.replace("6","",1)
            mydata[itemnum] = strnew
            print(strnew)
        if str.find(elementc, 0, 1) != -1:
            strnew = str + "   H"
            strnew = strnew.replace("1","",1)
            mydata[itemnum] = strnew
            print(strnew)
        if str.find(elementd, 0, 5) != -1:
            strnew = str + "   Au"
            strnew = strnew.replace("79","",1)
            mydata[itemnum] = strnew
            print(strnew)
        if str.find(elemente, 0, 5) != -1:
            strnew = str + "   Ru"
            strnew = strnew.replace("44","",1)
            mydata[itemnum] = strnew
            print(strnew)
        if str.find(elementf, 0, 5) != -1:
            strnew = str + "   N"
            strnew = strnew.replace("7 "," ",1)
            mydata[itemnum] = strnew
            print(strnew)
        if str.find(elementg, 0, 5) != -1:
            strnew = str + "   Ag"
            strnew = strnew.replace("47 "," ",1)
            mydata[itemnum] = strnew
            print(strnew)
        if str.find(elementh, 0, 5) != -1:
            strnew = str + "   O"
            strnew = strnew.replace("8 "," ",1)
            mydata[itemnum] = strnew
            print(strnew)
##        else:
##            mydata[itemnum] = str
##            print(str)
        itemnum += 1

    itemnum = 0

    
    for item in mydata:
        str = mydata[itemnum]
        strnew = "atom     " + str
        mydata[itemnum] = strnew
        itemnum += 1

titleline.append("# opt: au ".rstrip('\n'))
titleline = titleline + mydata


for item in titleline:
    f.writelines("%s\n" % item)

f.close()
    


