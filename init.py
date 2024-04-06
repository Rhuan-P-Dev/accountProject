
from fileSystemController import FileSystemController
from customLinkedListController import CustomLinkedListController
from objectController import ObjectController

FileSystem = FileSystemController()
Object = ObjectController()

import json

pathToAllObjects = "./static/allObjects/"

pathToMonthObjects = "monthObjects/"
pathToMonthsObjects = "monthsObjects/"
pathToInfObjects = "infObjects/"

accountsYear = 0
accountsMonth = 0

import logging
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

from flask import Flask, render_template
from flask_socketio import SocketIO, emit
app = Flask(__name__)
app.config['SECRET KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/accounts')
def accounts():
    return render_template('accounts.html')

@socketio.on('connect')
def do_connect():
    print("Client connected!")
    emit('from_server', {'cmd': 'connected'})

@socketio.on('message')
def get_message(msg):

    print("Data recieved:{0}".format(msg))
    # Submit action

    if(msg['cmd'] == 'saveMonthObjects'):
        # File 'format' {year}-{month}.txt
        # Create/update a file and storage/update this object
        # The content of file is a all objects of a year/month in specific

        if(len(msg['data']['objects']) == 0):
            return

        file = str(msg['data']['year'])+"-"+str(msg['data']['month'])+".txt"

        if(not FileSystem.checkFile(pathToAllObjects+pathToMonthObjects+file)):
            FileSystem.createFile(pathToAllObjects+pathToMonthObjects+file)
            FileSystem.writeFileTxt(pathToAllObjects+pathToMonthObjects+file, json.dumps(msg['data']['objects']))
            return
                
        
        monthObjects = json.loads(FileSystem.extractFileTxt(pathToAllObjects+pathToMonthObjects+file))

        for x in msg['data']['objects']:
            Object.typesOfObject[x['flag']](monthObjects, x)


        FileSystem.writeFileTxt(pathToAllObjects+pathToMonthObjects+file, json.dumps(monthObjects))
        
    elif(msg['cmd'] == 'saveMonthsObjects'):
        # Create/update a 'Months' CustomLinkedList data base with all objects

        monthsObjects = CustomLinkedListController(json.loads(FileSystem.extractFileTxt(pathToAllObjects+pathToMonthsObjects+"dataBase.txt")))

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

        FileSystem.writeFileTxt(pathToAllObjects+pathToMonthsObjects+"dataBase.txt", json.dumps(monthsObjects.returnLinkedList()))

    elif(msg['cmd'] == 'saveInfObjects'):
        # Create/update a 'inf' CustomLinkedList data base and with all objects

        infObjects = CustomLinkedListController(json.loads(FileSystem.extractFileTxt(pathToAllObjects+pathToInfObjects+"dataBase.txt")))

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
        
        FileSystem.writeFileTxt(pathToAllObjects+pathToInfObjects+"dataBase.txt", json.dumps(infObjects.returnLinkedList()))

    elif(msg['cmd'] == 'getAllYearData'):

        if(not FileSystem.checkFile(pathToAllObjects+pathToMonthsObjects+"dataBase.txt")):
            FileSystem.createFile(pathToAllObjects+pathToMonthsObjects+"dataBase.txt")
            temp = CustomLinkedListController({"head": {}})

            emptyObject = {}
            emptyObject['year'] = msg['data']
            emptyObject['months'] = []
            
            temp.add(emptyObject)

            FileSystem.writeFileTxt(pathToAllObjects+pathToMonthsObjects+"dataBase.txt", json.dumps(temp.returnLinkedList()))
            return

        if(not FileSystem.checkFile(pathToAllObjects+pathToInfObjects+"dataBase.txt")):
            FileSystem.createFile(pathToAllObjects+pathToInfObjects+"dataBase.txt")
            temp = CustomLinkedListController({"head": {}})

            emptyObject = {}
            emptyObject['year'] = msg['data']
            emptyObject['months'] = []
            
            temp.add(emptyObject)

            FileSystem.writeFileTxt(pathToAllObjects+pathToInfObjects+"dataBase.txt", json.dumps(temp.returnLinkedList()))
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
    if(FileSystem.checkFile(pathToFile)):
        return json.loads(open(pathToFile, 'r+').readlines()[0])
    else:
        return False

def sumAllMonthData(data):
    result = 0
    for x in data:
        result+= int((x['value'] * 100))
    return result / 100

def getAllMonthsData(year):
    dataBase = CustomLinkedListController(json.loads(FileSystem.extractFileTxt(pathToAllObjects+pathToMonthsObjects+"dataBase.txt")))

    month = 1
    monthsArray = []

    while month < 13:
        dataBaseResult = dataBase.Search(year,month,"month")
        if(not dataBaseResult == {'head': {}}):
            sumResult = CustomLinkedListController(dataBaseResult).sumAllYearsMonths()
        else:
            sumResult = 0
        monthsArray.append(sumResult)
        month += 1

    return monthsArray

def getAllInfData(year):
    dataBase = CustomLinkedListController(json.loads(FileSystem.extractFileTxt(pathToAllObjects+pathToInfObjects+"dataBase.txt")))

    month = 1
    infArray = []

    while month < 13:
        dataBaseResult = dataBase.Search(year,month,"inf")
        if(not dataBaseResult == {'head': {}}):
            sumResult = CustomLinkedListController(dataBaseResult).sumAllYearsInf()
        else:
            sumResult = 0
        infArray.append(sumResult)
        month += 1

    return infArray

def getMonthsAccounts(year, month):
    dataBaseResult = CustomLinkedListController(CustomLinkedListController(json.loads(FileSystem.extractFileTxt(pathToAllObjects+pathToMonthsObjects+"dataBase.txt"))).Search(year,month,"month"))

    if(not dataBaseResult.returnLinkedList() == {'head': {}}):
        arrayResult = dataBaseResult.toMonthsArray(year, month)
        if(arrayResult == []):
            arrayResult = False
    else:
        arrayResult = False

    return arrayResult

def getInfAccounts(year, month):
    dataBaseResult = CustomLinkedListController(CustomLinkedListController(json.loads(FileSystem.extractFileTxt(pathToAllObjects+pathToInfObjects+"dataBase.txt"))).Search(year,month,"inf"))

    if(not dataBaseResult.returnLinkedList() == {'head': {}}):
        arrayResult = dataBaseResult.toInfArray(year, month)
    else:
        arrayResult = False

    return arrayResult

if __name__ == "__main__":
    print("Server started!")
    print("You may now connect with a browser at http://127.0.0.1:5035/")
    socketio.run(app, host='127.0.0.1', port=5035)
    #socketio.run(app, host='192.168.1.5', port=5050)
    #socketio.run(app)