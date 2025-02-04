from time import perf_counter

fOut = open("times.csv", "w+")

#Create the header for the file
fOut.write(" , Add to Front, Add to Mid, Add to End, Remove from Front, Remove from Middle, Remove from End, Search Worst-Case\r\n")

def ListTests(demoList):
    #List add to front
    t1Start = perf_counter()
    demoList.insert(0, "a")
    t1Stop = perf_counter()

    #List add to middle
    mid = len(demoList)//2
    t2Start = perf_counter()
    demoList.insert(mid, "b")
    t2Stop = perf_counter()

    #List add to end
    t3Start = perf_counter()
    demoList.append("c")
    t3Stop = perf_counter()

    #List remove from front
    t4Start = perf_counter()
    demoList.pop(0)
    t4Stop = perf_counter()

    #List remove from middle
    t5Start = perf_counter()
    demoList.pop(mid)
    t5Stop = perf_counter()

    #List remove from end
    t6Start = perf_counter()
    demoList.pop()
    t6Stop = perf_counter()

    t1 = t1Stop - t1Start
    t2 = t2Stop - t2Start
    t3 = t3Stop - t3Start
    t4 = t4Stop - t4Start
    t5 = t5Stop - t5Start
    t6 = t6Stop - t6Start

    #search worst-case
    t7Start = perf_counter()
    toss = "DNE" in demoList
    t7Stop = perf_counter()
    t7 = t7Stop - t7Start
        

    fOut.write(f"{t1},{t2},{t3},{t4},{t5},{t6},{t7}\r\n")

def dictionaryTests(demoDic):
    #add to dictionary
    t1Start = perf_counter()
    demoDic["a"] = "A"
    t1Stop = perf_counter()
    t1 = t1Stop - t1Start

    #remove from a dictionary
    t2Start = perf_counter()
    demoDic["b"] = "B"
    t2Stop = perf_counter()
    t2 = t2Stop - t2Start

    #Worst Case Search
    t3Start = perf_counter()
    toss = "DNE" in demoDic
    t3Stop = perf_counter()
    t3 = t3Stop - t3Start

    fOut.write(f"{t1},n/a,n/a,{t2},n/a,n/a,{t3}\r\n")

#generate & test Lists
for x in range(1,26):
    fOut.write(f"{2**x},")
    tempList = []
    for x in range(2**x):
        tempList.append(x)

    ListTests(tempList)

#generate & test Dictionaries
for x in range(1,26):
    fOut.write(f"{2**x},")
    tempDict = {}
    for x in range(2**x):
        tempDict[x] = x

    dictionaryTests(tempDict)


fOut.close()








