file=open("input.txt","w")
file.write("Hello, This is a file handling example.")
file.close()

file=open("input.txt","r")
content=file.read()
print(content)
file.close()
try:
    #use with open() to read the file
    with open("inputs.txt","r") as file:
        content=file.read()
        print(content)
except FileNotFoundError:
    print("File not found")


#csv file reading
import csv
with open("data.csv","r") as file:
    reader=csv.reader(file)
    for row in reader:
        print(row[0],row[1])

#excel file reading without pandas
#import openpyxl
#workbook=openpyxl.load_workbook("data.xlsx")
#sheet=workbook.active
#for row in sheet.iter_rows(values_only=True):
#    print(row[0],row[1])

#excel file reading with pandas
import pandas as pd
df=pd.read_excel("data.xlsx")
print(df)