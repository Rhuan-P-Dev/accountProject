
from customLinkedListController import CustomLinkedListController
from fileSystemController import FileSystemController
from pathController import PathController

Path = PathController()
FileSystem = FileSystemController()
CustomLinkedList = CustomLinkedListController()

import json

class AccountsInfoController:

    def createMonthObject(self, month, start, end, objects):
        monthObject = {}
        monthObject['month'] = month
        monthObject['SE'] = []
        monthObject['SE'].append({
            'start':start,
            'end':end,
            'objects':objects,
        })
        return monthObject

    def createInfObject(self, month, objects, infObject = {}):
        infObject['month'] = month
        infObject['objects'] = objects
        return infObject
        
    def getAllMonthData(self, year):
        index = 0
        monthsArray = []
        while index < 12:
            allMonthData = self.getMonthAccounts(year,(index+1))
            if(allMonthData):
                monthDataSum = self.sumAllMonthData(allMonthData)
            else:
                monthDataSum = 0
            monthsArray.append(monthDataSum)
            index+=1
        return monthsArray

    def getMonthAccounts(self, year, month):
        pathToFile = Path.pathToMonthObjects+(f"{year}-{month}.txt")
        if(FileSystem.checkFile(pathToFile)):
            return json.loads(open(pathToFile, 'r+').readlines()[0])
        else:
            return False

    def sumAllMonthData(self, data):
        result = 0
        for x in data:
            result+= int((x['value'] * 100))
        return result / 100

    def getAllMonthsData(self, year):
        dataBase = CustomLinkedListController(json.loads(FileSystem.extractFileTxt(Path.pathToMonthsObjects+"dataBase.txt")))

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

    def getAllInfData(self, year):
        dataBase = CustomLinkedListController(json.loads(FileSystem.extractFileTxt(Path.pathToInfObjects+"dataBase.txt")))

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

    def getMonthsAccounsts(self, year, month):
        dataBaseResult = CustomLinkedListController(CustomLinkedListController(json.loads(FileSystem.extractFileTxt(Path.pathToMonthsObjects+"dataBase.txt"))).Search(year,month,"month"))

        if(not dataBaseResult.returnLinkedList() == {'head': {}}):
            arrayResult = dataBaseResult.toMonthsArray(year, month)
            if(arrayResult == []):
                arrayResult = False
        else:
            arrayResult = False

        return arrayResult

    def getInfAccounts(self, year, month):
        dataBaseResult = CustomLinkedListController(CustomLinkedListController(json.loads(FileSystem.extractFileTxt(Path.pathToInfObjects+"dataBase.txt"))).Search(year,month,"inf"))

        if(not dataBaseResult.returnLinkedList() == {'head': {}}):
            arrayResult = dataBaseResult.toInfArray(year, month)
        else:
            arrayResult = False

        return arrayResult

