class CurrentReadings():
    def __init__(self,numbers_string_input):
        self.inputCurrentRange = numbers_string_input
        self.Current_readings_list = []
        self.CurrentRangeFrequencyDcn = {}

    def extractNumbersList(self):
        self.Current_readings_list = list(map(int,self.inputCurrentRange.split(",")))
        self.Current_readings_list.sort()
        #print(self.numbers_list)
        return(self.Current_readings_list)

    def updateRangeFreqDcn(self, lower_number,higher_number,currentCount):
        dcn_key = str(lower_number)+"-"+str(higher_number)
        self.CurrentRangeFrequencyDcn[dcn_key] = str(currentCount)

    def generateRangeFrequencyData(self):
        self.Current_readings_list.sort()
        if(len(self.Current_readings_list) >0):
            lower_number = self.Current_readings_list[0]
            higher_number = lower_number
            currentCount =0
            for current_Amp in self.Current_readings_list:
                if(higher_number in range(current_Amp-1,current_Amp+1)):
                    higher_number = current_Amp
                    currentCount +=1
                else:
                    self.updateRangeFreqDcn(lower_number,higher_number,currentCount)
                    currentCount = 1
                    lower_number = higher_number = current_Amp
            self.updateRangeFreqDcn(lower_number,higher_number,currentCount)

    def exportCSV(self):
        print("Range, Readings")
        testText = "Range, Readings\n"
        for currentRange in self.CurrentRangeFrequencyDcn:
            print(currentRange,",",self.CurrentRangeFrequencyDcn[currentRange])
            testText=testText+ currentRange+","+self.CurrentRangeFrequencyDcn[currentRange] +"\n"
        return(testText)
    
    def getAmpereReadingsList(self,sensorNum):
        numbersList = self.extractNumbersList()
        convertedList = []
        for reading in numbersList:
            convertedList.append(self.convertToReadingList(sensorNum,reading))
                #print(convertedList)

        self.Current_readings_list = convertedList

    def convertToReadingList(self, sensorNum,reading):
        if(sensorNum ==1):
            return(int(round(self.convertADCReadingToAmpereSensor1(reading),0)))
        elif(sensorNum ==2):
            return(abs(int(round(self.convertADCReadingToAmpereSensor2(reading),0))))

    def convertADCReadingToAmpereSensor1(self,reading):
        if reading in range(0,4095):
            return((reading/4094)*10)
    
    def convertADCReadingToAmpereSensor2(self,reading):
        if reading in range(0,1023):
            return(round(((reading/1023)*30.03)-15,3))
'''
if __name__ == '__main__':
    CurrentReadingsObject = CurrentReadings(inputCurrentReadings)
    CurrentReadingsObject.generateRangeFrequencyData()
    print(CurrentReadingsObject.exportCSV())
'''