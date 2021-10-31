import pandas as pd
import plotly.express as px
import csv

file = open("File1.csv", newline = "")
reader = csv.reader(file)
filedata = list(reader)
filedata.pop(0)
totalmarks = 0
totalentries = len(filedata)

for i in filedata:
    totalmarks += float(i[1])

mean = totalmarks/totalentries
print("Mean Is : " + str(mean))

df = pd.read_csv("File1.csv")
graph = px.scatter(df,x = "Student Number", y = "Marks")
graph.update_layout(shapes = [dict(type = "line", y0 = mean, y1 = mean, x0 = 0, x1 = totalentries)])
graph.show()
