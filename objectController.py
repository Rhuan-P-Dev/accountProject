
class ObjectController:

    def __init__(self):
        self.typesOfObject = {
            "add": self.add,
            "update": self.update,
            "remove": self.remove
        }

    def add(self, array, object):
        array.append(object)

    def update(self, array, object):
        index = 0
        for x in array:
            if(x["ID"] == object["ID"]):
                array[index] = object
                return
            index+=1

    def remove(self, array, object):
        index = 0
        for x in array:
            if(x["ID"] == object["ID"]):
                del array[index]
                return
            index+=1