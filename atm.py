class Atm(object):
    bankbalance = 50000
    widraw = 10000
    def __init__ (self,name,cardnumber,pin,bankname):
        self.name = name
        self.pin = pin
        self.bankname = bankname
        self.cardnumber = cardnumber
    def getdetails(self):
        print(self.name,self.cardnumber,self.pin,self.bankname)
    bankbalance = input(bankbalance)
    widraw = input(widraw)
kamlesh = Atm("kamlesh",6969696969,6969,"TharaBank")   
print(kamlesh.getdetails()) 