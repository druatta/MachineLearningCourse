import numpy as np
import matplotlib.pyplot as plt
from pandas import DataFrame


def readExcelSheet1(excelfile):
    from pandas import read_excel
    return (read_excel(excelfile)).values

print("Hello, world!")