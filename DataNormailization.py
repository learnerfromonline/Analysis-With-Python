'''
We are Normailize the values based on the certain factors
for suppose if a column contains a value in between 10000 to 70000
its impossible to make a graph or any operations on it,
so in that tyype of the situations the normilization helps us to analysis the data effictively
'''
import  pandas as pd
df = pd.read_csv("C:/Ram's Works/Online Learning/COURSERA/IBM DATA SCIENCE/Data Analysis with python/Files/archive/car_price_prediction.csv")
print(df.iloc[3])
# So while see the datafram we conside the price value ,just assume.we perform normilization on the price
# There are so many methods are there to normalize the data
# first method is:simple-feature-scaling
df["Price"]=df["Price"]/max(df["Price"])
print(df.iloc[3])
# Second Method is :Min-Max
df1 = pd.read_csv("C:/Ram's Works/Online Learning/COURSERA/IBM DATA SCIENCE/Data Analysis with python/Files/archive/car_price_prediction.csv")
print(df1.iloc[4])
df1["Price"]=((df1["Price"]-min(df1["Price"]))/(max(df1["Price"])-min(df1["Price"])))
print(df1.iloc[4])
# While applying the two methods i observe that both will gave the same value of price after applying normilazition
# The Third Method Called:z-score
df3 = pd.read_csv("C:/Ram's Works/Online Learning/COURSERA/IBM DATA SCIENCE/Data Analysis with python/Files/archive/car_price_prediction.csv")
print(df3.iloc[5])
df3["Price"]=(df3["Price"]-df3["Price"].mean())/df3["Price"].std()
print(df3.iloc[5])
# BY The Z-score the values are different from first nd second techniques

