
class FileSystemController:

    def checkFile(self, pathToFile):
        try:
            with open(pathToFile, 'r') as f:
                return True
        except IOError:
            return False

    def createFile(self, pathToFile):
        file = open(pathToFile, 'w+')
        file.close()

    def extractFileTxt(self, pathToFile):
        file = open(pathToFile, 'r+')
        txt = file.readlines()[0]
        file.close()
        return txt

    def writeFileTxt(self, pathToFile, txt):
        file = open(pathToFile, 'w+')
        file.writelines(txt)
        file.close()
        return True