
from RequestValidate import RequestValidate

class TransactionRequestBean(RequestValidate):
    # def __init__(self):
    #     RequestValidate.__init__(self)

    tilda = "~"

    separator = "|"

    requestType= ""

    merchantCode = ""

    merchantTxnRefNumber = ""

    ITC = "jai"

    amount = ""

    accountNo = ""

    currencyCode = ""

    uniqueCustomerId = ""

    returnURL = ""

    s2SReturnURL = ""

    TPSLTxnID = ""

    shoppingCartDetails = ""

    txnDate = ""

    email = "jai@"

    mobileNumber = ""

    socialMediaIdentifier = ""

    bankCode = ""

    customerName = ""

    reqst = None


    webServiceLocator = "NA"

    MMID = ""

    OTP = ""

    key= None #####

    iv=None#####

    mkd= None #####

    blockSize = 128

    mode = "cbc"

    logPath = ""

    currDate= None ######

    rqst_kit_vrsn = 1

    custId = ""

    cardId = ""

    cardNo = ""

    cardName = ""

    cardCVV = ""

    cardExpMM = ""

    cardExpYY = ""

    timeOut = 30



    def __set(self, field, value):
        self.field = value

    def __get(self, variable):
        return self.variable

    def getTilda(self):
        return self.tilda

    def getseparator(self):
        return self.separator

    def getUniqueCustomerId(self):
        return self.uniqueCustomerId

    def getEmail(self):
        return self.email

    def getSocialMediaIdentifier(self):
        return self.socialMediaIdentifier

    def getReqst(self):
        return self.reqst

    def getWebServiceLocator(self):
        return self.getWebServiceLocator

    def getMkd(self):
        return self.mkd

    def getBlockSize(self):
        return self.blockSize

    def getMode(self):
        return self.mode

    def getLogPath(self):
        return self.logPath


    def getCurrDate(self):
        return self.currDate

    def getRqst_kit_vrsn(self):
        return self.rqst_kit_vrsn

    def getTimeOut(self):
        return self.timeOut

    def setTilda(self, tilda):
        self.tilda = tilda
        # print(self.tilda)

    def setUniqueCustomerId(self, uniqueCustomerId):
        self.uniqueCustomerId = uniqueCustomerId

    def setEmail(self,  email):
        self.email = email
        # print(self.email)    
    def setSocialMediaIdentifier(self, socialMediaIdentifier):
        self.socialMediaIdentifier = socialMediaIdentifier

    def setReqst(self, reqst):
        self.reqst = reqst


    def setWebServiceLocator(self, webServiceLocator):
        self.webServiceLocator = webServiceLocator

    def setMkd(self, mkd): 
        self.mkd = mkd
        print(self.mkd)

    def setBlockSizes(self, blockSize):
        self.blockSize = blockSize

    def setMode(self, mode):
        self.mode = mode

    def setLogPath(self, logPath):
        self.logPath = logPath

    def setCurrDate(self, currDate):
        self.currDate = currDate

    def setRqst_kit_vrsn(self, rqst_kit_vrsn):
        self.rqst_kit_vrsn = rqst_kit_vrsn




    def getEncryptedData(self):
        clientMetaData = "abcd"

        if  not self.isBlankOrNull(self.ITC):
            # print(True)
            clientMetaData = clientMetaData + "{itc:" + self.ITC + "}"                
            # print(clientMetaData)

        if  not self.isBlankOrNull(self.email):
            # print(True)
            clientMetaData = clientMetaData + "{email:" + self.email + "}"                
            # print(clientMetaData)

        if  not self.isBlankOrNull(self.mobileNumber):
            # print(True)
            clientMetaData = clientMetaData + "{mob:" + self.mobileNumber + "}"                
            # print(clientMetaData)

        if  not self.isBlankOrNull(self.uniqueCustomerId):
            # print(True)
            clientMetaData = clientMetaData + "{custid:" + self.uniqueCustomerId + "}"                
            # print(clientMetaData)
        
        if  not self.isBlankOrNull(self.customerName):
            # print(True)
            clientMetaData = clientMetaData + "{custname:" + self.customerName + "}"                
            # print(clientMetaData)
            
        self.strReqst = ""
        # print(self.-strReqst)
        if not self.isBlankOrNull(self.requestType):
            self.strReqst + "rqst_type=" + self.requestType

        self.strReqst + "|rqst_kit_vrsn=1.0." + str(self.rqst_kit_vrsn)
        # print(x)
        if not self.isBlankOrNull(self.merchantCode):
            self.strReqst + "|tpsl_clnt_cd=" + self.merchantCode
           

        if not self.isBlankOrNull(self.accountNo): 
            self.strReqst + "|accountNo=" + self.accountNo
            

        if not self.isBlankOrNull(self.merchantTxnRefNumber): 
            self.strReqst + "|clnt_txn_ref=" + self.merchantTxnRefNumber
            

        if not self.isBlankOrNull(clientMetaData): 
            self.strReqst + "|clnt_rqst_meta=" + clientMetaData
            # print(x)


        if not self.isBlankOrNull(self.amount): 
            self.strReqst + "|rqst_amnt=" + self.amount
        

        if not self.isBlankOrNull(self.currencyCode):
            self.strReqst + "|rqst_crncy=" + self.currencyCode
        

        if not self.isBlankOrNull(self.returnURL):
            self.strReqst + "|rtrn_url=" + self.returnURL
        

        if not self.isBlankOrNull(self.s2SReturnURL):
            self.strReqst + "|s2s_url=" + self.s2SReturnURL
        

        if not self.isBlankOrNull(self.shoppingCartDetails):
            self.strReqst + "|rqst_rqst_dtls=" + self.shoppingCartDetails
        
        if not self.isBlankOrNull(self.txnDate): 
            self.strReqst + "|clnt_dt_tm=" + self.txnDate
        

        if not self.isBlankOrNull(self.bankCode):
            self.strReqst + "|tpsl_bank_cd=" + self.bankCode
        

        if not self.isBlankOrNull(self.TPSLTxnID): 
            self.strReqst + "|tpsl_txn_id=" + self.TPSLTxnID
        

        if not self.isBlankOrNull(self.custId):
            self.strReqst + "|cust_id=" + self.custId
        

        if not self.isBlankOrNull(self.cardId): 
            self.strReqst + "|card_id=" + self.cardId
        

        if not self.isBlankOrNull(self.mobileNumber):
            self.strReqst + "|mob=" + self.mobileNumber
        
        if self.requestType == "TWC" or self.requestType == "TRC" or self.requestType == "TIC":
            




x = TransactionRequestBean()
x.getEncryptedData()

