'''
Bins are used to identify the certain range from a data
like 0-50 :low
     51-100:medium
     101-400:high
where initially the data is in between those ranges
while applying the bin method it is easily to identify for us in which range the value is present
it is helpful in data analysis and visiualization
ex:for suppose we have 1500 rows are there
if we plot the values the screen is very clumzy
so after applying the bin we can change the values into three groups
low,medium and high
so we can easily estimate the result by viewing the graph

'''
import pandas as pd
import numpy as np
df = pd.read_csv("C:\\Ram's Works\\Online Learning\\COURSERA\\IBM DATA SCIENCE\\Data Analysis with python\\Files\\archive\\car_price_prediction.csv")
print(df.iloc[2])
bins = np.linspace(df["Price"].min(),df["Price"].max(),4)
groups = ["LOW","MEDIUM","HIGH"]
labels = pd.cut(df["Price"],bins,labels=groups,include_lowest=True)
print(labels)
print(df["Price"].max())