
from fileSystemController import FileSystemController
from customLinkedListController import CustomLinkedListController
from objectController import ObjectController
from pathController import PathController
from accountsInfoController import AccountsInfoController

FileSystem = FileSystemController()
Object = ObjectController()
Path = PathController()
AccountsInfo = AccountsInfoController()

import json

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

        if(not FileSystem.checkFile(Path.pathToMonthObjects+file)):
            FileSystem.createFile(Path.pathToMonthObjects+file)
            FileSystem.writeFileTxt(Path.pathToMonthObjects+file, json.dumps(msg['data']['objects']))
            return
        
        monthObjects = json.loads(FileSystem.extractFileTxt(Path.pathToMonthObjects+file))

        for x in msg['data']['objects']:
            Object.typesOfObject[x['flag']](monthObjects, x)

        FileSystem.writeFileTxt(Path.pathToMonthObjects+file, json.dumps(monthObjects))
        
    elif(msg['cmd'] == 'saveMonthsObjects'):
        # Create/update a 'Months' CustomLinkedList data base with all objects

        monthsObjects = CustomLinkedListController(json.loads(FileSystem.extractFileTxt(Path.pathToMonthsObjects+"dataBase.txt")))

        # check if the element exists if there is no creating the element, if everything is ok just modify the objects
        if(monthsObjects.thisYearExist(msg['data']['year'])):

            if(monthsObjects.thisMonthExist(msg['data']['year'],msg['data']['month'])):

                if(monthsObjects.thisSEExist(msg['data']['year'],msg['data']['month'],msg['data']['start'],msg['data']['end'])):
                    
                    for x in msg['data']['objects']:
                        monthsObjects.Object(msg['data']['year'],msg['data']['month'],msg['data']['start'],msg['data']['end'],x,x['flag'])
                else:
                    monthsObjects.addSE(msg['data']['year'],msg['data']['month'],{"start":msg['data']['start'],"end":msg['data']['end'],"objects":msg['data']['objects']})

            else:
                monthsObjects.addMonth(msg['data']['year'],AccountsInfo.createMonthObject(msg['data']['month'],msg['data']['start'],msg['data']['end'],msg['data']['objects']))
        else:

            emptyObject = {}
            emptyObject['year'] = msg['data']['year']
            emptyObject['months'] = []
            emptyObject['months'].append(AccountsInfo.createMonthObject(msg['data']['month'],msg['data']['start'],msg['data']['end'],msg['data']['objects']))

            monthsObjects.add(emptyObject)

        FileSystem.writeFileTxt(Path.pathToMonthsObjects+"dataBase.txt", json.dumps(monthsObjects.returnLinkedList()))

    elif(msg['cmd'] == 'saveInfObjects'):
        # Create/update a 'inf' CustomLinkedList data base and with all objects

        infObjects = CustomLinkedListController(json.loads(FileSystem.extractFileTxt(Path.pathToInfObjects+"dataBase.txt")))

        # check if the element exists if there is no creating the element, if everything is ok just modify the objects
        if(infObjects.thisYearExist(msg['data']['year'])):

            if(infObjects.thisMonthExist(msg['data']['year'],msg['data']['month'])):

                for x in msg['data']['objects']:
                    infObjects.ObjectInf(msg['data']['year'],msg['data']['month'],x,x['flag'])

            else:
                infObjects.addMonth(msg['data']['year'],AccountsInfo.createInfObject(msg['data']['month'],msg['data']['objects']))
        else:

            emptyObject = {}
            emptyObject['year'] = msg['data']['year']
            emptyObject['months'] = []
            emptyObject['months'].append(AccountsInfo.createInfObject(msg['data']['month'],msg['data']['objects']))

            infObjects.add(emptyObject)
        
        FileSystem.writeFileTxt(Path.pathToInfObjects+"dataBase.txt", json.dumps(infObjects.returnLinkedList()))

    elif(msg['cmd'] == 'getAllYearData'):

        monthArray = AccountsInfo.getAllMonthData(msg['data'])
        monthsArray = AccountsInfo.getAllMonthsData(msg['data'])
        infArray = AccountsInfo.getAllInfData(msg['data'])

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
        emit('from_server', {'cmd': 'initSite', 'year': accountsYear, 'month': accountsMonth})

    elif(msg['cmd'] == 'getAccounts'):
        finalArray = []

        finalArray.append(AccountsInfo.getMonthAccounts(msg['year'],msg['month']))

        finalArray.append(AccountsInfo.getMonthsAccounsts(msg['year'], msg['month']))

        finalArray.append(AccountsInfo.getInfAccounts(msg['year'], msg['month']))

        emit('from_server', {'cmd': 'loadAccounts', 'accounts': finalArray})

def initDataBases():

    if(not FileSystem.checkFile(Path.pathToMonthsObjects+"dataBase.txt")):
        FileSystem.createFile(Path.pathToMonthsObjects+"dataBase.txt")
        temp = CustomLinkedListController({"head": {}})

        emptyObject = {}
        emptyObject['year'] = 0
        emptyObject['months'] = []
            
        temp.add(emptyObject)

        FileSystem.writeFileTxt(Path.pathToMonthsObjects+"dataBase.txt", json.dumps(temp.returnLinkedList()))
        return

    if(not FileSystem.checkFile(Path.pathToInfObjects+"dataBase.txt")):
        FileSystem.createFile(Path.pathToInfObjects+"dataBase.txt")
        temp = CustomLinkedListController({"head": {}})

        emptyObject = {}
        emptyObject['year'] = 0
        emptyObject['months'] = []
            
        temp.add(emptyObject)

        FileSystem.writeFileTxt(Path.pathToInfObjects+"dataBase.txt", json.dumps(temp.returnLinkedList()))
        return

if __name__ == "__main__":

    initDataBases()

    print("Server started!")
    print("You may now connect with a browser at http://127.0.0.1:5035/")
    socketio.run(app, host='127.0.0.1', port=5035)
    #socketio.run(app, host='192.168.1.5', port=5050)
    #socketio.run(app)