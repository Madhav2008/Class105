import pandas as pd
import plotly.express as px
import csv
import math

file = open("File2.csv", newline = "")
reader = csv.reader(file)
filedata = list(reader)
data = filedata[0]

def mean():
    totalmarks = 0
    totalentries = len(data)

    for i in data:
        totalmarks += int(i)

    mean = totalmarks/totalentries
    print("Mean Is : " + str(mean))

    return mean

squaredlist = []

for number in data:
    a = int(number) - mean()
    a = a**2
    squaredlist.append(a)

sum = 0

for i in squaredlist:
    sum = sum + i

result = sum/(len(data) - 1)
standarddeviation = math.sqrt(result)
print("Standard Deviation Is : " + str(standarddeviation))
