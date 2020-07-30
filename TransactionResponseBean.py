from RequestValidate import RequestValidate
# from AES import AES

class TransactionResponseBean(RequestValidate):

    responsePayload = ""

    key= None

    iv= None

    logPath = ""

    blocksize = 128

    mode = "cbc"

    acbd = ''


    def set(self, field, value):
        # print(self._key)
        self.field = value
        print(value)
    # def get(self, variable):
    #     print(self.variable)

    def getLogPath(self):
        return self.logPath       

    def getBlocksize(self):
        return self.blocksize

    def getMode(self):
        return self.mode

    def setResponsePayload(self, responsePayload):
        self.responsePayload =  responsePayload

    def setLogPath(self, logPath):
        self.logPath = logPath

    def setBlocksize(self, blocksize):
        self.blocksize =  blocksize

    def setMode(self, mode):
        self.mode = mode



    def getResponsePayload(self):

        responseParams = {
                'pRes': self.responsePayload,
                'pEncKey': self.key,
                'pEncIv': self.iv
        }

        errorResponse = self.validateResponseParam(responseParams)

            if errorResponse:
                return errorResponse;
            

x=TransactionResponseBean()
x.set()