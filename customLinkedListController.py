
from objectController import ObjectController

Object = ObjectController()

import copy

class CustomLinkedListController:

    def __init__(self, list = {"head": {}}):
        self.list = list
        self.typesOfSearch = {
            "month": self.searchMonths,
            "inf": self.searchInf
        }

    def returnLinkedList(self):
        return self.list

    def checkValidMonth(self, object):

        if("month" in object):
            if("SE" in object):
                for account in object["SE"]:
                    if(
                        not isinstance(account["start"], int)
                        or
                        not isinstance(account["end"], int)
                        or
                        not account["start"] <= account["end"]
                    ):
                        return False
            
        else:
            return False

        return True

    def checkValidMonths(self, object):

        for month in object["months"]:
            if(not self.checkValidMonth(month)):
                return False

        return True

    def checkValidAddInput(self, object):

        if(
            "year" in object
            and
            self.checkValidMonths(object)
        ):

            return True
        else:
            return False

    # this list is self-adjusted to keep in a growing order
    def add(self, value):

        if(not self.checkValidAddInput(value)):
            return False

        if(self.list["head"] == {}):
            self.list["head"]["value"] = value
            self.list["head"]["next"] = "null"
        else:
            node = self.list["head"]
            while True:
                if(node["value"]["year"] > value["year"]):
                    oldValue = node["value"]
                    oldNext = node["next"]
                    node["value"] = value
                    node["next"] = {"value":oldValue,"next":oldNext}
                    return True
                else:
                    if(node["next"] == "null"):
                        node["next"] = {}
                        node["next"]["value"] = value
                        node["next"]["next"] = "null"
                        return True
                    node = node["next"]
    
    # search on the self.list and create a list from the results
    def search(self, year, month, type):

        tempCustomLinkedList = CustomLinkedListController({"head": {}})

        node = self.list["head"]

        while True:

            searchResult = self.typesOfSearch[type](node["value"], year, month)

            if(not searchResult == "null"):
                tempCustomLinkedList.add(searchResult)

            if(node["next"] == "null"):
                return tempCustomLinkedList.returnLinkedList()
            else:
                node = node["next"]

    # adds nodes that the range 'start' and 'end', are high or equal from the search range
    def searchMonths(self, node, year, month):
        node2 = copy.deepcopy(node)
        if(node["year"] <= year):
            indexMonth = 0
            for x in node["months"]:
                indexSE = 0
                for y in x["SE"]:
                    path = ( y["end"] - y["start"] ) + x["month"]
                    cut = ( ( year - node["year"] ) * 12 ) + month
                    if( path < cut or node["year"] == year and x["month"] > month):
                        del node2["months"][indexMonth]["SE"][indexSE]
                        indexSE-=1
                    indexSE+=1
                indexMonth+=1
            return node2
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

        while True:
            if(n["value"]["year"] == year):
                for x in n["value"]["months"]:
                    if(x["month"] == month):
                        for y in x["SE"]:
                            if(y["start"] == start and y["end"] == end):
                                return Object.typesOfObject[type](y["objects"], object)

            if(n["next"] == "null"):
                return False
            else:
                n = n["next"]

    def ObjectInf(self, year, month, object, type):

        n = self.list["head"]

        while True:
            if(n["value"]["year"] == year):
                for x in n["value"]["months"]:
                    if(x["month"] == month):
                        return Object.typesOfObject[type](x["objects"], object)

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
                        tempObj = self.calcTheEvolution(year, month, n["value"]["year"], months["month"], SE["start"], SE["end"])
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

    def calcTheEvolution(self, searchYear, searchMonth, year, month, start, end):
        path = (end - start) + month
        cut = ( (searchYear - year) * 12 ) + searchMonth
        diff = path - cut
        evolution = ( (path - month) - diff ) + start

        return {"start":evolution, "end":end, "month":month}