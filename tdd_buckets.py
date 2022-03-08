
inputCurrentReadings = '3, 3, 5, 4, 10, 11, 12,15,19,17,21,11,14,1,27'
#Expected {'1-1': 1, '3-5': 4, '10-12': 4, '14-15': 2, '17-17': 1, '19-19': 1, '21-21': 1, '27-27': 1}
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
        self.extractNumbersList()
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
'''
if __name__ == '__main__':
    CurrentReadingsObject = CurrentReadings(inputCurrentReadings)
    CurrentReadingsObject.generateRangeFrequencyData()
    print(CurrentReadingsObject.exportCSV())
'''
    