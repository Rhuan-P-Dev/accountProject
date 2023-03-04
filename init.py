# base of kobold ai 
# https://github.com/KoboldAI/KoboldAI-Client

import copy
import json 
import random



pathToAllObjects = "./static/allObjects/"

pathToMonthObjects = "monthObjects/"
pathToMonthsObjects = "monthsObjects/"
pathToInfObjects = "infObjects/"


accountsYear = 0
accountsMonth = 0


# Terminal tags for colored text
class colors:
    PURPLE    = '\033[95m'
    BLUE      = '\033[94m'
    CYAN      = '\033[96m'
    GREEN     = '\033[92m'
    YELLOW    = '\033[93m'
    RED       = '\033[91m'
    END       = '\033[0m'
    UNDERLINE = '\033[4m'


# Start flask & SocketIO
print("{0}Initializing Flask... {1}".format(colors.PURPLE, colors.END), end="")
from flask import Flask, render_template
from flask_socketio import SocketIO, emit
app = Flask(__name__)
app.config['SECRET KEY'] = 'secret!'
socketio = SocketIO(app)
print("{0}OK!{1}".format(colors.GREEN, colors.END))

# Set up Flask routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/accounts')
def accounts():
    return render_template('accounts.html')

# Class

class CustomLinkedList:

    def __init__(self, list = {"head": {}}):
        self.list = list

    def returnLinkedList(self):
        return self.list
    
    # this list is self-adjusted to keep in a growing order
    def add(self, value):
        if(self.list["head"] == {}):
            self.list["head"]["value"] = value
            self.list["head"]["next"] = "null"
        else:
            n = self.list["head"]
            while True:
                if(n["value"]["year"] > value["year"]):
                    oldValue = n["value"]
                    oldNext = n["next"]
                    n["value"] = value
                    n["next"] = {"value":oldValue,"next":oldNext}
                    return
                else:
                    while True:
                        if(n["next"] == "null"):
                            n["next"] = {}
                            n["next"]["value"] = value
                            n["next"]["next"] = "null"
                            return
                        else:
                            n = n["next"]
                            break
    
    # search on the self.list and create a list from the results
    def Search(self, year, month, type):
        typesOfSearch = {"month":self.searchMonths,"inf":self.searchInf}

        tempCustomLinkedList = CustomLinkedList({"head": {}})
        temp = ""

        n = self.list["head"]

        while True:

            temp = typesOfSearch[type](n["value"], year, month)

            if(not temp == "null"):
                tempCustomLinkedList.add(temp)

            if(n["next"] == "null"):
                return tempCustomLinkedList.returnLinkedList()
            else:
                n = n["next"]

    # adds nodes that the range 'start' and 'end', are high or equal from the search range
    def searchMonths(self, n, year, month):
        n2 = copy.deepcopy(n)
        if(n["year"] <= year):
            indexMonth = 0
            for x in n["months"]:
                indexSE = 0
                for y in x["SE"]:
                    path = ( y["end"] - y["start"] ) + x["month"]
                    cut = ( ( year - n["year"] ) * 12 ) + month
                    if( path < cut or n["year"] == year and x["month"] > month):
                        del n2["months"][indexMonth]["SE"][indexSE]
                        indexSE-=1
                    indexSE+=1
                indexMonth+=1
            return n2
        return "null"

    # adds nodes that are smaller than the search value
    def searchInf(self, n, year, month):
        n = copy.deepcopy(n)
        if(n["year"] < year):
            return n
        if(n["year"] == year):
            index = 0
            for x in n["months"]:
                if(x["month"] > month):
                    del n["months"][index]
                index+=1
            if(len(n["months"]) == 0):
                return "null"
            return n

        return "null"

    # add, remove, update a Object
    def Object(self, year, month, start, end, object, type):

        n = self.list["head"]
        OB = ObjectControler()

        typesOfObject = {"remove":OB.objectRemove,"add":OB.objectAdd,"update":OB.objectUpdate}

        while True:
            if(n["value"]["year"] == year):
                for x in n["value"]["months"]:
                    if(x["month"] == month):
                        for y in x["SE"]:
                            if(y["start"] == start and y["end"] == end):
                                return typesOfObject[type](y["objects"], object)

            if(n["next"] == "null"):
                return False
            else:
                n = n["next"]

    def ObjectInf(self, year, month, object, type):

        n = self.list["head"]
        OB = ObjectControler()

        typesOfObject = {"remove":OB.objectRemove,"add":OB.objectAdd,"update":OB.objectUpdate}

        while True:
            if(n["value"]["year"] == year):
                for x in n["value"]["months"]:
                    if(x["month"] == month):
                        return typesOfObject[type](x["objects"], object)

            if(n["next"] == "null"):
                return False
            else:
                n = n["next"]

    def thisYearExist(self, year):
        n = self.list["head"]
        while True:
            if(n["value"]["year"] == year):
                return True
            if(n["next"] == "null"):
                return False
            n = n["next"]

    def thisMonthExist(self, year, month):
        n = self.list["head"]
        while True:
            if(n["value"]["year"] == year):
                for x in n["value"]["months"]:
                    if(x["month"] == month):
                        return True
                return False
            if(n["next"] == "null"):
                return False
            n = n["next"]

    def addMonth(self, year, month):
        n = self.list["head"]
        while True:
            if(n["value"]["year"] == year):
                n["value"]["months"].append(month)
                return True
            if(n["next"] == "null"):
                return False
            n = n["next"]

    def thisSEExist(self, year, month, start, end):
        n = self.list["head"]
        while True:
            if(n["value"]["year"] == year):
                for x in n["value"]["months"]:
                    if(x["month"] == month): 
                        for y in x["SE"]:
                            if(y["start"] == start and y["end"] == end):
                                return True
                    return False
            if(n["next"] == "null"):
                return False
            n = n["next"]

    def addSE(self, year, month, SE):
        n = self.list["head"]
        while True:
            if(n["value"]["year"] == year):
                for x in n["value"]["months"]:
                    if(x["month"] == month): 
                        x["SE"].append(SE)
                        return True
            if(n["next"] == "null"):
                return False
            n = n["next"]

    def sumAllYearsMonths(self):
        n = self.list["head"]
        result = 0
        while True:
            for months in n["value"]["months"]:
                for SE in months["SE"]:
                    for objects in SE["objects"]:
                        result+= int((objects["value"] * 100))
            if(n["next"] == "null"):
                return result / 100
            n = n["next"]
    
    def sumAllYearsInf(self):
        n = self.list["head"]
        result = 0
        while True:
            for months in n["value"]["months"]:
                for objects in months["objects"]:
                    result+= int((objects["value"] * 100))
            if(n["next"] == "null"):
                return result / 100
            n = n["next"]

    def toMonthsArray(self, year, month):
        n = self.list["head"]
        array = []
        while True:
            for months in n["value"]["months"]:
                for SE in months["SE"]:
                    for objects in SE["objects"]:
                        tempObj = calcTheEvolution(year, month, n["value"]["year"], months["month"], SE["start"], SE["end"])
                        objects["start"] = tempObj["start"]
                        objects["end"] = tempObj["end"]
                        objects["month"] = tempObj["month"]
                        objects["year"] = n["value"]["year"]
                        objects["type"] = "months"
                        array.append(objects)
            if(n["next"] == "null"):
                return array
            n = n["next"]

    def toInfArray(self, year, month):
        n = self.list["head"]
        array = []
        while True:
            for months in n["value"]["months"]:
                for objects in months["objects"]:
                    objects["month"] = months["month"]
                    objects["year"] = n["value"]["year"]
                    objects["type"] = "inf"
                    array.append(objects)
            if(n["next"] == "null"):
                return array
            n = n["next"]




class ObjectControler:

    def objectRemove(self, array, object):
        index = 0
        for x in array:
            if(x["ID"] == object["ID"]):
                del array[index]
                return
            index+=1

    def objectAdd(self, array, object):
        array.append(object)
    
    def objectUpdate(self, array, object):
        index = 0
        for x in array:
            if(x["ID"] == object["ID"]):
                array[index] = object
                return
            index+=1


#==================================================================#
# Event triggered when browser SocketIO is loaded and connects to server
#==================================================================#
@socketio.on('connect')
def do_connect():
    print("{0}Client connected!{1}".format(colors.GREEN, colors.END))
    emit('from_server', {'cmd': 'connected'})

#==================================================================#
# Event triggered when browser SocketIO sends data to the server
#==================================================================#



@socketio.on('message')
def get_message(msg):

    print("{0}Data recieved:{1}{2}".format(colors.GREEN, msg, colors.END))
    # Submit action

    if(msg['cmd'] == 'saveMonthObjects'):
        # File 'format' {year}-{month}.txt
        # Create/update a file and storage/update this object
        # The content of file is a all objects of a year/month in specific

        if(len(msg['data']['objects']) == 0):
            return

        file = str(msg['data']['year'])+"-"+str(msg['data']['month'])+".txt"

        if(not checkFile(pathToAllObjects+pathToMonthObjects+file)):
            createFile(pathToAllObjects+pathToMonthObjects+file)
            writeFileTxt(pathToAllObjects+pathToMonthObjects+file, json.dumps(msg['data']['objects']))
            return
                
        
        monthObjects = json.loads(extractFileTxt(pathToAllObjects+pathToMonthObjects+file))

        OB = ObjectControler()
        typesOfObject = {"remove":OB.objectRemove,"add":OB.objectAdd,"update":OB.objectUpdate}

        for x in msg['data']['objects']:
            typesOfObject[x['flag']](monthObjects, x)


        writeFileTxt(pathToAllObjects+pathToMonthObjects+file, json.dumps(monthObjects))
        
    elif(msg['cmd'] == 'saveMonthsObjects'):
        # Create/update a 'Months' CustomLinkedList data base with all objects

        monthsObjects = CustomLinkedList(json.loads(extractFileTxt(pathToAllObjects+pathToMonthsObjects+"dataBase.txt")))

        # check if the element exists if there is no creating the element, if everything is ok just modify the objects
        if(monthsObjects.thisYearExist(msg['data']['year'])):

            if(monthsObjects.thisMonthExist(msg['data']['year'],msg['data']['month'])):

                if(monthsObjects.thisSEExist(msg['data']['year'],msg['data']['month'],msg['data']['start'],msg['data']['end'])):
                    
                    for x in msg['data']['objects']:
                        monthsObjects.Object(msg['data']['year'],msg['data']['month'],msg['data']['start'],msg['data']['end'],x,x['flag'])
                else:
                    monthsObjects.addSE(msg['data']['year'],msg['data']['month'],{"start":msg['data']['start'],"end":msg['data']['end'],"objects":msg['data']['objects']})

            else:
                monthsObjects.addMonth(msg['data']['year'],createMonthObject(msg['data']['month'],msg['data']['start'],msg['data']['end'],msg['data']['objects']))
        else:

            emptyObject = {}
            emptyObject['year'] = msg['data']['year']
            emptyObject['months'] = []
            emptyObject['months'].append(createMonthObject(msg['data']['month'],msg['data']['start'],msg['data']['end'],msg['data']['objects']))

            monthsObjects.add(emptyObject)

        writeFileTxt(pathToAllObjects+pathToMonthsObjects+"dataBase.txt", json.dumps(monthsObjects.returnLinkedList()))

    elif(msg['cmd'] == 'saveInfObjects'):
        # Create/update a 'inf' CustomLinkedList data base and with all objects

        infObjects = CustomLinkedList(json.loads(extractFileTxt(pathToAllObjects+pathToInfObjects+"dataBase.txt")))

        # check if the element exists if there is no creating the element, if everything is ok just modify the objects
        if(infObjects.thisYearExist(msg['data']['year'])):

            if(infObjects.thisMonthExist(msg['data']['year'],msg['data']['month'])):

                for x in msg['data']['objects']:
                    infObjects.ObjectInf(msg['data']['year'],msg['data']['month'],x,x['flag'])

            else:
                infObjects.addMonth(msg['data']['year'],createInfObject(msg['data']['month'],msg['data']['objects']))
        else:

            emptyObject = {}
            emptyObject['year'] = msg['data']['year']
            emptyObject['months'] = []
            emptyObject['months'].append(createInfObject(msg['data']['month'],msg['data']['objects']))

            infObjects.add(emptyObject)
        
        writeFileTxt(pathToAllObjects+pathToInfObjects+"dataBase.txt", json.dumps(infObjects.returnLinkedList()))

    elif(msg['cmd'] == 'getAllYearData'):

        if(not checkFile(pathToAllObjects+pathToMonthsObjects+"dataBase.txt")):
            createFile(pathToAllObjects+pathToMonthsObjects+"dataBase.txt")
            temp = CustomLinkedList({"head": {}})

            emptyObject = {}
            emptyObject['year'] = msg['data']
            emptyObject['months'] = []
            
            temp.add(emptyObject)

            writeFileTxt(pathToAllObjects+pathToMonthsObjects+"dataBase.txt", json.dumps(temp.returnLinkedList()))
            return

        if(not checkFile(pathToAllObjects+pathToInfObjects+"dataBase.txt")):
            createFile(pathToAllObjects+pathToInfObjects+"dataBase.txt")
            temp = CustomLinkedList({"head": {}})

            emptyObject = {}
            emptyObject['year'] = msg['data']
            emptyObject['months'] = []
            
            temp.add(emptyObject)

            writeFileTxt(pathToAllObjects+pathToInfObjects+"dataBase.txt", json.dumps(temp.returnLinkedList()))
            return

        monthArray = getAllMonthData(msg['data'])
        monthsArray = getAllMonthsData(msg['data'])
        infArray = getAllInfData(msg['data'])

        index = 0
        finalArray = []

        while index < 12:
            finalArray.append( (int( (monthArray[index] * 100) ) + int( (monthsArray[index] * 100) ) + int( (infArray[index] * 100) ) ) / 100)
            index+=1

        emit('from_server', {'cmd': 'allYearData', 'data': finalArray})
        
    elif(msg['cmd'] == 'setAccountsData'):
        global accountsYear
        global accountsMonth

        accountsYear = msg['year']
        accountsMonth = msg['month']

    elif(msg['cmd'] == 'getAccountsData'):
        emit('from_server', {'cmd': 'initSite', 'year':accountsYear, 'month':accountsMonth})

    elif(msg['cmd'] == 'getAccounts'):
        finalArray = []

        finalArray.append(getMonthAccounts(msg['year'],msg['month']))

        finalArray.append(getMonthsAccounts(msg['year'], msg['month']))

        finalArray.append(getInfAccounts(msg['year'], msg['month']))

        emit('from_server', {'cmd': 'loadAccounts', 'accounts': finalArray})
        

def checkFile(pathToFile):
    try:
        with open(pathToFile, 'r') as f:
            return True
    except IOError:
        return False


def createFile(pathToFile):
    arquivo = open(pathToFile, 'w+')
    arquivo.close()

def extractFileTxt(pathToFile):
    fileTxt = open(pathToFile, 'r+')
    txt = fileTxt.readlines()[0]
    fileTxt.close()
    return txt

def writeFileTxt(pathToFile, txt):
    fileTxt = open(pathToFile, 'w+')
    fileTxt.writelines(txt)
    fileTxt.close()
    return True

def createMonthObject(month, start, end, objects):
    monthObject = {}
    monthObject['month'] = month
    monthObject['SE'] = []
    monthObject['SE'].append({
        'start':start,
        'end':end,
        'objects':objects,
    })
    return monthObject

def createInfObject(month, objects, infObject = {}):
    infObject['month'] = month
    infObject['objects'] = objects
    return infObject
    
def getAllMonthData(year):
    index = 0
    monthsArray = []
    while index < 12:
        allMonthData = getMonthAccounts(year,(index+1))
        if(allMonthData):
            monthDataSum = sumAllMonthData(allMonthData)
        else:
            monthDataSum = 0
        monthsArray.append(monthDataSum)
        index+=1
    return monthsArray

def getMonthAccounts(year, month):
    pathToFile = pathToAllObjects+pathToMonthObjects+(f"{year}-{month}.txt")
    if(checkFile(pathToFile)):
        return json.loads(open(pathToFile, 'r+').readlines()[0])
    else:
        return False

def sumAllMonthData(data):
    result = 0
    for x in data:
        result+= int((x['value'] * 100))
    return result / 100

def getAllMonthsData(year):
    dataBase = CustomLinkedList(json.loads(extractFileTxt(pathToAllObjects+pathToMonthsObjects+"dataBase.txt")))

    month = 1
    monthsArray = []

    while month < 13:
        dataBaseResult = dataBase.Search(year,month,"month")
        if(not dataBaseResult == {'head': {}}):
            sumResult = CustomLinkedList(dataBaseResult).sumAllYearsMonths()
        else:
            sumResult = 0
        monthsArray.append(sumResult)
        month += 1

    return monthsArray

def getAllInfData(year):
    dataBase = CustomLinkedList(json.loads(extractFileTxt(pathToAllObjects+pathToInfObjects+"dataBase.txt")))

    month = 1
    infArray = []

    while month < 13:
        dataBaseResult = dataBase.Search(year,month,"inf")
        if(not dataBaseResult == {'head': {}}):
            sumResult = CustomLinkedList(dataBaseResult).sumAllYearsInf()
        else:
            sumResult = 0
        infArray.append(sumResult)
        month += 1

    return infArray

def getMonthsAccounts(year, month):
    dataBaseResult = CustomLinkedList(CustomLinkedList(json.loads(extractFileTxt(pathToAllObjects+pathToMonthsObjects+"dataBase.txt"))).Search(year,month,"month"))

    if(not dataBaseResult.returnLinkedList() == {'head': {}}):
        arrayResult = dataBaseResult.toMonthsArray(year, month)
        if(arrayResult == []):
            arrayResult = False
    else:
        arrayResult = False

    return arrayResult


def calcTheEvolution(searchYear, searchMonth, year, month, start, end):
        path = (end - start) + month
        cut = ( (searchYear - year) * 12 ) + searchMonth
        diff = path - cut
        evolution = ( (path - month) - diff ) + start

        return {"start":evolution, "end":end, "month":month}

def getInfAccounts(year, month):
    dataBaseResult = CustomLinkedList(CustomLinkedList(json.loads(extractFileTxt(pathToAllObjects+pathToInfObjects+"dataBase.txt"))).Search(year,month,"inf"))

    if(not dataBaseResult.returnLinkedList() == {'head': {}}):
        arrayResult = dataBaseResult.toInfArray(year, month)
    else:
        arrayResult = False

    return arrayResult

#==================================================================#
#  Final startup commands to launch Flask app
#==================================================================#
if __name__ == "__main__":
    # Start Flask/SocketIO (Blocking, so this must be last method!)
    print("{0}Server started!\rYou may now connect with a browser at http://127.0.0.1:5035/{1}".format(colors.GREEN, colors.END))
    socketio.run(app, host='0.0.0.0', port=5035)
    #socketio.run(app)