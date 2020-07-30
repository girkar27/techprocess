from zeep import Client

class AES:
    M_CBC = 'cbc'
    M_CFB = 'cfb'
    M_ECB = 'ecb'
    M_NOFB = 'nofb'
    M_OFB = 'ofb'
    M_STREAM = 'stream'
    AES_CIPHER_128 = 'aes-128'
    AES_CIPHER_192 = 'aes-192'
    AES_CIPHER_256 = 'aes-256'


    def __init__(self, data=None, key=None, blockSize=None, mode=None, iv=None):
        self.data = data
        self.key = key
        self.blockSize = blockSize
        self.mode = mode
        self.iv = iv

    def set(self, field, value):
        # self.field = value
        # print(value)
        # switcher={
        #     'cipher': 'self.value',
        #     'mode': "self.jai"
        # }
        if field =='cipher':
            self.field = self.setBlockSize(value)
        elif field =='mode':
            self.field = self.setMode(value)

            # print(self.field)
        else:
            # print("nothing")
            self.field = value

    # def get(self, variable):

    #             # print/(switcher.get(field, 'nothing'))

    def setBlockSize(self, value):
        if value ==128:
            cipher = self.AES_CIPHER_128 
        if value == 192:
            cipher = self.AES_CIPHER_192
        if value ==256:
            cipher = self.AES_CIPHER_256

        return cipher
        # print(cipher)
    def setMode(self, value):
        if value == self.M_CBC:
            mode = self.M_CBC

        if value == self.M_CFB:
            mode = self.M_CFB
        
        if value == self.M_ECB:
            mode = self.M_ECB
    
        if value == self.M_NOFB:
            mode = self.M_NOFB

        if value == self.M_OFB:
            mode = self.M_OFB
        
        if value == self.M_STREAM:
            mode = self.M_STREAM

        else:
            mode = self.M_ECB

        # print(mode)
        return mode

    def validateParams(self):
        if self.data != None and self.key != None and self.cipher != None:
            return True

        else:
            return False
        

x = AES()
x.validateParams()


# wsdl = 'http://www.soapclient.com/xml/soapresponder.wsdl'
# client = Client(wsdl=wsdl)
# print(client.service.Method1('Zeep', 'is cool'))


