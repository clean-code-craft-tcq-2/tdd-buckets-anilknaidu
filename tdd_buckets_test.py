import unittest
from tdd_buckets import CurrentReadings

currentReadingsTest = CurrentReadings("4,5")

class tdd_buckets_test(unittest.TestCase):
  def test_generateRangeFrequencyData(self):
    currentReadingsTest.generateRangeFrequencyData()
    self.assertTrue(currentReadingsTest.CurrentRangeFrequencyDcn["4-5"]=="2")
        
  def test_csv_data(self):
      currentReadingsTest.generateRangeFrequencyData()
      self.assertTrue(currentReadingsTest.exportCSV()=="Range, Readings\n4-5,2\n")
  
if __name__ =="__main__":
    unittest.main()