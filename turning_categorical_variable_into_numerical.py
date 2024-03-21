'''
As we already know that an model dosent calculate the categorical data.
so we need to change the categorical data into numerical data.
ther is one method in python ""pd.get_dummies()""
this method helps us to change the categorical into numerical data by assigning 1,if the element present in the row
or else 0 ,how many unique elements are ther in the column it create the individual column for each element
and assign the values 1 or 0 based on the presence

'''
import pandas as pd

df = pd.read_csv("C:\\Ram's Works\\Online Learning\\COURSERA\\IBM DATA SCIENCE\\Data Analysis with python\\Files\\archive\\car_price_prediction.csv")
print(df.iloc[1])
pd.set_option("display.max_columns",None)
print(df.describe())
'''
    In the dataframe there is a column called Color.
    I dont know the how many elemnts are there in the column
    If i want to know i use ".unique()" option 
    It will give the how many elements present in the column.
    If i want to Know the length of the column i use the len(.unique())
'''
print(df["Color"].unique())
print(pd.get_dummies(df["Color"])) # There in therminal the get dummy values are displaye in true and false if the element is present in the row it appears as true otherwise false
'''
    I have a Question that there is a column called Mileage where the data type is object.
    And end of the value of the column element contains "km" thats why its object.
    If i want to convert it into int firstly, i need to remove the "km"
    How can i remove by using rstrip() method we can did it.
    This method can eliminates the white spaces and the defined string.
'''
df["Mileage"]=pd.to_numeric(df["Mileage"].str.rstrip("km"))#where the km is removed
df["Mileage"]=df["Mileage"].astype("int")
print(df.iloc[1])
print(df.dtypes)# the data type is also changed.