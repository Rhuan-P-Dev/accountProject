
class ObjectController:

    def __init__(self):
        self.typesOfObject = {
            "add": self.add,
            "update": self.update,
            "remove": self.remove
        }

    def checkValidAddInput(self, object):
        if(
            "ID" in object
            and
            object["ID"].startswith("ID")
        ):
            return True
        return False

    def add(self, array, object):
        if self.checkValidAddInput(object):
            array.append(object)

    def update(self, array, object):
        for index, x in enumerate(array):
            if x["ID"] == object["ID"]:
                array[index] = object
                return True
        return False

    def remove(self, array, object):
        index = 0
        for x in array:
            if(x["ID"] == object["ID"]):
                del array[index]
                return
            index+=1