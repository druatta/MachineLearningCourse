import ExcelSheet
import numpy as Num
import matplotlib.pyplot as Plot
from pandas import DataFrame

ExcelData = None

ExcelSheet.ReadExcelSheet()
SheetNames = ExcelSheet.GetSheetNames()
ExcelData = ExcelSheet.ReadExcelData()

ArrayOfAllData = Num.array((ExcelData[:,0]*12+ExcelData[:,1]), dtype = float)