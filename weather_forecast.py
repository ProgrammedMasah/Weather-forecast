def LoadDataFromFile(path):
    try:
        lines = open(path,'r').readlines()
        lines = lines = [ i.strip().split(sep=" ")  for i in lines ]
        return [ [lines[i][0],float(lines[i][1])]  for i in range(0,len(lines))  if len(lines[i][0]) > 0 ] 
    except Exception as exc:
        print(exc)
        return [[" ",0]]
def ToFah(C):
    return C * 1.8 + 32

def getTempF(Temp):
    return [ [Temp[i][0],ToFah(Temp[i][1])] for i in range(0,len(Temp)) ]

def getHgt80(Humidity):
    return list(filter(lambda x : x[:][1] > 80, Humidity ))

def getTlt45(TempF):
    return list(filter(lambda x : x[:][1] < 45, TempF ))

def getRain100(rainfall):
    return list(filter(lambda x : x[:][1] > 100, rainfall ))

def getRainy(Hgt80, Tlt45, Raingt100):
    Rainy = {}
    Tlt = dict(Tlt45)
    Raingt = dict(Raingt100)
    for i in range(0, len(Hgt80)): 
        if Hgt80[i][0] in Tlt.keys():
            if Hgt80[i][0] in Raingt.keys():
                Rainy [Hgt80[i][0]] = [Hgt80[i][1], Tlt[Hgt80[i][0]], Raingt[Hgt80[i][0]]]
    return Rainy

def printRainy(Rainy):
    city = list(Rainy.keys())
    info = list(Rainy.values())
    print("%10s %15s %15s %15s"%("City", "Humidity", "Temp", "Rainfall"))
    print("=" * 70)
    for i in range (0, len(city)):
        print("%10s %15s %15s %15s"%(city[i], info[i][0], info[i][1], info[i][2]))

Temp = LoadDataFromFile("Temp.txt")
Humidity = LoadDataFromFile("Humidity.txt")
rainfall = LoadDataFromFile("rainfall.txt")

TempF = getTempF(Temp)

Hgt80 = getHgt80(Humidity)
Tlt45 = getTlt45(TempF)
Raingt100 = getRain100(rainfall)

Rainy = getRainy(Hgt80, Tlt45, Raingt100)
    
printRainy(Rainy)

        
        
