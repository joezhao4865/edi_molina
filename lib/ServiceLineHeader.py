class ServiceLineHeader:
    def __init__(self, dilimiter, lineIndex, procedureCode, billedAmount, units, serviceZip, diagPointers, rangedService = False, repeatedService = False):
        self.dilimiter = dilimiter
        self.lineIndex = str(lineIndex)
        self.sv101_1 = 'HC'
        self.sv101_2 = procedureCode
        self.sv101_3 = ('', ':UB')[rangedService]
        self.sv101_4 = ('', ':76')[repeatedService]
        self.billedAmt = str(billedAmount)
        self.unit = 'UN'
        self.unitCount = str(int(units))
        self.serviceLocationCode = ('12', '11')[serviceZip == '22066'] 
        self.sv106 = ''
        self.diagCodePointer = diagPointers # primary
        
    
    def getSegment(self):
        procedureCode = self.sv101_1+':'+self.sv101_2+self.sv101_3 + self.sv101_4
        
        return self.dilimiter.join(['LX*'+self.lineIndex+'~', '*'.join(['SV1', procedureCode, self.billedAmt, self.unit, self.unitCount, self.serviceLocationCode, self.sv106, self.diagCodePointer+'~'])])