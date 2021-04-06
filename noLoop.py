class repeatString:
    def repeatString(self, oldString):
        self.newString = 'XXXXXXXXXX'
        self.newString = self.newString.replace(self.newString[0], self.newString)
        self.newString = self.newString.replace(self.newString[0], self.newString)

    def changeName(self, name):
        self.newString = self.newString.replace(self.newString[0], name)

    def fixEndString(self, name):
        self.newString = self.newString[:-(len(name)+4)] + ' e ' + name + '.'

    def getNewString(self):
        return self.newString

class milRenatosComLoop:
    def __init__(self, StringToReplace):
        self.loopDont = self.noLoop(StringToReplace)

    def noLoop(self, StringToReplace):
        actualName = StringToReplace + ', '
        string = repeatString()
        string.repeatString(actualName)
        string.changeName(actualName)
        string.fixEndString(StringToReplace)

        print(string.getNewString())

if __name__ == '__main__':
    withoutLoop = milRenatosComLoop('Renato')
    withoutLoop.loopDont