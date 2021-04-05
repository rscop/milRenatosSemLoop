class repeatString:
    def repeatString(self, oldString):
        self.newString = oldString[0:9].replace(oldString[0], oldString[0:9])
        self.newString = self.newString.replace(self.newString[0], self.newString[0:9])

    def changeName(self, name):
        self.newString = self.newString.replace(self.newString[0], name)

    def fixEndString(self):
        self.newString = self.newString[:-10] + ' e Renato.'

    def getNewString(self):
        return self.newString

class milRenatosComLoop:
    def __init__(self, StringToReplace):
        self.loopDont = self.noLoop(StringToReplace)

    def noLoop(self, StringToReplace):
        string = repeatString()
        string.repeatString(StringToReplace)
        string.changeName(StringToReplace[10:])
        string.fixEndString()

        print(string.getNewString())

if __name__ == '__main__':
    withoutLoop = milRenatosComLoop('XXXXXXXXXXRenato, ')
    withoutLoop.loopDont