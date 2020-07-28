

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


    def __init__(self, data=None, key=None, blockSize=None, mode=None, iv):
    	self.data = data
    	self.key = key
    	self.blockSize = blockSize
    	self.mode = mode
    	self.iv = iv


