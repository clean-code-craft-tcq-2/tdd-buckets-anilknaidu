import unittest
from tdd_buckets import CurrentReadings

currentReadingsTestSnsr1 = CurrentReadings("21,1313,3231,0921")
currentReadingsTestSnsr1.getAmpereReadingsList(1)

currentReadingsTestSnsr2 = CurrentReadings("0,511,1022")
currentReadingsTestSnsr2.getAmpereReadingsList(2)

class tdd_buckets_test(unittest.TestCase):
  
  def test_generateRangeFrequencyData(self):
    currentReadingsTestSnsr1.generateRangeFrequencyData()
    currentReadingsTestSnsr2.generateRangeFrequencyData()
    self.assertTrue(currentReadingsTestSnsr1.CurrentRangeFrequencyDcn["2-3"]=="2")
    self.assertTrue(currentReadingsTestSnsr2.CurrentRangeFrequencyDcn["15-15"]=="2")
  
  def test_csv_data(self):
      currentReadingsTestSnsr1.generateRangeFrequencyData()
      currentReadingsTestSnsr2.generateRangeFrequencyData()
      self.assertTrue(currentReadingsTestSnsr1.exportCSV()=="Range, Readings\n0-0,1\n2-3,2\n8-8,1\n")
      self.assertTrue(currentReadingsTestSnsr2.exportCSV()=="Range, Readings\n0-0,1\n15-15,2\n")

  def test_convertADCReadingToAmpereSensors(self):
    epsilon = 0.01
    #boundarytesting
    self.assertAlmostEqual(currentReadingsTestSnsr2.convertADCReadingToAmpereSensor2(511),0,delta=epsilon)
    self.assertAlmostEqual(currentReadingsTestSnsr1.convertADCReadingToAmpereSensor1(1024),2.5,delta=epsilon)
    self.assertAlmostEqual(currentReadingsTestSnsr2.convertADCReadingToAmpereSensor2(0),-15,delta=epsilon)
    self.assertAlmostEqual(currentReadingsTestSnsr1.convertADCReadingToAmpereSensor1(0),0,delta=epsilon)
    self.assertAlmostEqual(currentReadingsTestSnsr2.convertADCReadingToAmpereSensor2(1022),15,delta=epsilon)
    self.assertAlmostEqual(currentReadingsTestSnsr1.convertADCReadingToAmpereSensor1(4093),10,delta=epsilon)


if __name__ =="__main__":
    unittest.main()