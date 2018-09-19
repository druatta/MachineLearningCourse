import numpy as np
import matplotlib.pyplot as plt
from pandas import DataFrame

def readExcelSheet1(excelfile):
    from pandas import read_excel
    return (read_excel(excelfile)).values

def readExcelRange(excelfile,sheetname="Sheet1",startrow=1,endrow=1,startcol=1,endcol=1):
    from pandas import read_excel
    values=(read_excel(excelfile, sheetname,header=None)).values;
    return values[startrow-1:endrow,startcol-1:endcol]

def readExcel(excelfile,**args):
    if args:
        data=readExcelRange(excelfile,**args)
    else:
        data=readExcelSheet1(excelfile)
    if data.shape==(1,1):
        return data[0,0]
    elif (data.shape)[0]==1:
        return data[0]
    else:
        return data
        
def writeExcelData(x,excelfile,sheetname,startrow,startcol):
    from pandas import DataFrame, ExcelWriter
    from openpyxl import load_workbook
    df=DataFrame(x)
    book = load_workbook(excelfile)
    writer = ExcelWriter(excelfile, engine='openpyxl') 
    writer.book = book
    writer.sheets = dict((ws.title, ws) for ws in book.worksheets)
    df.to_excel(writer, sheet_name=sheetname,startrow=startrow-1, startcol=startcol-1, header=False, index=False)
    writer.save()
    writer.close()

def getSheetNames(excelfile):
    from pandas import ExcelFile
    return (ExcelFile(excelfile)).sheet_names

def Build1DHistogramClassifier(X,T,B,xmin,xmax):
    HF=np.zeros(B).astype('int32');
    HM=np.zeros(B).astype('int32');
    binindices=(np.round(((B-1)*(X-xmin)/(xmax-xmin)))).astype('int32');
    for i,b in enumerate(binindices):
        if T[i]=='Female':
            HF[b]+=1;
        else:
            HM[b]+=1;
    return [HF, HM]

def Apply1DHistogramClassifier(queries,HF,HM,xmin,xmax):
    B=np.alen(HF);
    binindices=np.clip((np.round(((B-1)*(queries-xmin)/(xmax-xmin)))).astype('int32'),0,B-1);
    countF=HF[binindices];
    countM=HM[binindices];
    resultlabel=np.full(np.alen(binindices),"Indeterminate",dtype=object);
    resultprob=np.full(np.alen(binindices),np.nan,dtype=object);
    indicesF=countF>countM;
    indicesM=countM>countF;
    resultlabel[indicesF]="Female";
    resultlabel[indicesM]="Male";
    probF=countF/(countF+countM);
    probM=countM/(countF+countM);
    resultprob[indicesF]=probF[indicesF];
    resultprob[indicesM]=probM[indicesM];
    return resultlabel, resultprob
    
excelfile=r"/home/ec2-user/environment/AssignmentOne/Daniel Ruatta - Assignment 1.xlsx";

sheets=getSheetNames(excelfile);sheets

data=readExcel(excelfile)
X=np.array(data[:,0]+data[:,1],dtype=float)
T=np.array([str(g) for g in data[:,2]])

queries=((readExcel(excelfile,
                  sheetname='Queries',
                  startrow=3,
                  endrow=8,
                  startcol=1,
                  endcol=1)).astype(float)).ravel();

B=32;
xmin=np.amin(X);
xmax=np.amax(X);
[HF,HM]=Build1DHistogramClassifier(X,T,B,xmin,xmax);

plt.figure(figsize=(10,5));
opacity = 0.5
[bincenters,binwidth]=np.linspace(xmin, xmax, num=B, retstep=True);
rects1 = plt.bar(bincenters-(binwidth/2), HF, binwidth,
                 alpha=opacity,
                 color='pink',
                 edgecolor='black',
                 label='Female')
rects2 = plt.bar(bincenters+(binwidth/2), HM, binwidth,
                 alpha=opacity,
                 color='b',
                 edgecolor='black',
                 label='Male')
plt.xlabel('Height')
plt.ylabel('Count')
plt.xticks(bincenters, bincenters.astype('int32'), fontsize=10)
plt.legend()
plt.show()

[resultHlabel, resultHprob]=Apply1DHistogramClassifier(queries,HF,HM,xmin,xmax)

print '\n', (DataFrame([resultHlabel, resultHprob]).T)

print '\n' "xmin = ", xmin

print '\n' 'xmax = ', xmax

print '\n' "Program complete."

print '\n', queries