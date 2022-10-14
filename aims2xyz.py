import re
f = open("geometry.xyz", "w")
mylines = []
mydata = []
linenum=0
startindex = 0
endindex = 0
itemnum = 0
with open ("aims.dft.out", "rt") as myfile:
    for myline in myfile:
        linenum += 1
        mylines.append(myline.rstrip('\n'))
        substra = "Final atomic structure"
        substrb = "Final output of selected total energy values:"
        if myline.find(substra) != -1:
            startindex = linenum
        elif myline.find(substrb) != -1:
            endindex = linenum - 3
        else:
            continue
    linenum = 0
for myline in mylines:
    linenum += 1
    if (linenum > startindex and linenum < endindex):
        mydata.append(myline)
    else:
        continue

itemnum = 0
for item in mydata:
    str = mydata[itemnum]
    strnew = str.replace("atom","")
    mydata[itemnum] = strnew
    itemnum += 1

# Searches aims.dft.out atoms for the chemical symbol and replaces wih number in front.
# If you need to add additional elements, add additional elementi, elementj, ...
# Also add additional if loops:
#       elif str.find(elemente) != -1:
#           strnew = "44" + str
#           strnew = strnew.replace("Ru","")
#           mydata[itemnum] = strnew

itemnum = 0
for item in mydata:
    str = mydata[itemnum]
    elementa = "Fe"
    elementb = "C"
    elementc = "H"
    elementd = "Au"
    elemente = "Ru"
    elementf = "N"
    elementg = "Ag"
    elementh = "V"
    elementi = "O"


    if str.find(elementa) != -1:
        strnew = "26" + str
        strnew = strnew.replace("Fe","")
        mydata[itemnum] = strnew
        #print(strnew)
    elif str.find(elementb) != -1:
        strnew = "6" + str
        strnew = strnew.replace("C","")
        mydata[itemnum] = strnew
        print(strnew)
    elif str.find(elementc) != -1:
        strnew = "1" + str
        strnew = strnew.replace("H","")
        mydata[itemnum] = strnew
        print(strnew)
    elif str.find(elementd) != -1:
        strnew = "79" + str
        strnew = strnew.replace("Au","")
        mydata[itemnum] = strnew
        print(strnew)
    elif str.find(elementi) != -1:
        strnew = "8" + str
        strnew = strnew.replace("O","")
        mydata[itemnum] = strnew
        print(strnew)
    elif str.find(elemente) != -1:
        strnew = "44" + str
        strnew = strnew.replace("Ru","")
        mydata[itemnum] = strnew
        print(strnew)
    elif str.find(elementf) != -1:
        strnew = "7" + str
        strnew = strnew.replace("N","")
        mydata[itemnum] = strnew
        print(strnew)
    elif str.find(elementg) != -1:
        strnew = "47" + str
        strnew = strnew.replace("Ag","")
        mydata[itemnum] = strnew
        print(strnew)
    elif str.find(elementh) != -1:
        strnew = "23" + str
        strnew = strnew.replace("V","")
        mydata[itemnum] = strnew
        print(strnew)
    else:
        print(str)
        mydata[itemnum] = str
    itemnum += 1
        
        
del mydata[0]



for item in mydata:
    f.writelines("%s\n" % item)
f.close()

            


