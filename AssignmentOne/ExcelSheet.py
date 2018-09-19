import numpy as Numpy
import matplotlib.pyplot as Plot
from pandas import DataFrame

ExcelFileWithData = "/home/ec2-user/environment/AssignmentOne/Daniel Ruatta - Assignment 1.xlsx"
HeightAndGenderData = None
FirstSheet = "Data"
FirstRow = 1
LastRow = 1
FirstColumn = 1
LastColumn = 1


def ReadExcelSheet():
    from pandas import read_excel
    return (read_excel(ExcelFileWithData)).values

def GetSheetNames():
    from pandas import ExcelFile
    return (ExcelFile(ExcelFileWithData)).sheet_names
    
def ReadExcelRange():
    from pandas import read_excel
    Values = (read_excel(ExcelFileWithData, FirstSheet, header = None)).values;
    return Values[FirstRow - 1: LastRow, FirstColumn - 1:LastColumn]
    
def ReadExcelData(**Arguments):
    if Arguments is not None:
        ExcelData = ReadExcelRange(**Arguments)
    else:
        ExcelData = ReadExcelSheet()
    if ExcelData.shape == (1,1):
        return ExcelData[0,0]
    elif (ExcelData.shape)[0] == 1:
        return ExcelData[0]
    else:
        return ExcelData