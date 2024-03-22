import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
'''file_path="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-SkillsNetwork/labs/Data%20files/auto.csv"
headers = ["symboling","normalized-losses","make","fuel-type","aspiration", "num-of-doors","body-style",
         "drive-wheels","engine-location","wheel-base", "length","width","height","curb-weight","engine-type",
         "num-of-cylinders", "engine-size","fuel-system","bore","stroke","compression-ratio","horsepower",
         "peak-rpm","city-mpg","highway-mpg","price"]
df = pd.read_csv(file_path,names=headers)
df.to_csv("car_dataset.csv")'''
#on above code is for to take the csv file into my project
df = pd.read_csv("car_dataset.csv")
print(df.iloc[2])

# there are some '?' values are there so i need to change it to nan
''' 
    for now i want to findout "?" the symbol present in which rows
    so i use .isin() method for target lock and .any() method for is there or not
    
'''
print(df.isin(["?"]).any())
print(df[df["stroke"]=="?"]) #here the stroke column contains "?" so i want to retrive the corresponding rows
#       #to replace with "?" with NaN
df.replace('?',np.nan,inplace=True)
print(df)
print(df.isin(["?"]).any()) #to check if any values are there or not after implementing the operation the o/p gives false means all are replaced
def checknull():
    missing = df.isnull()
    for cm in missing.columns.tolist():
        print(cm)
        print(missing[cm].value_counts())
        print("")

'''
    we have see that some columns have missing values ,
    one column is "normalized-losses" in the column ther are totally 
    4 missing values are there so we need to replace with mean.
'''
avgmean=df["normalized-losses"].astype("float").mean(axis=0)
df["normalized-losses"].replace(np.nan,avgmean,inplace=True) # we replace the value succesfully.
print(df.iloc[2]) #where the row 2 have initially NaN after replace it changes

'''
    The column num-of-doors has 2 NaN values those are in the type of object
    if its the number we findout what is the maximum value on the column but its string .
    in that case we need to calculate the maximum value present in the column.
    with the help of value_counts() its possible and findout the maximum occureance .idmax() helpful for this scenario
     
'''
numofdoors=df["num-of-doors"].value_counts().idxmax()
df["num-of-doors"].replace(np.nan,numofdoors,inplace=True)

'''
    The column "bore" has totally 4 empty Values.
    so replace with the mean
'''
df["bore"].replace(np.nan,df["bore"].astype("float").mean(axis=0),inplace=True)
checknull() #checknull is a userdefined function to check the missing values replaced or not

'''
    The column stroke has 4 NaN values.
    This is in the type:float
    replace empty values with mean
    axis=0 refers the row 
    axis=1 refers tthe column 
    inplace=True refers change the edits direactly in the dataset.
    
'''
df["stroke"].replace(np.nan,df["stroke"].astype("float").mean(axis=0),inplace=True)
checknull()

'''
    The column horsepower has 2 empty columns.
    replace it by mean
'''
df["horsepower"].replace(np.nan,df["horsepower"].astype("float").mean(axis=0),inplace=True)
checknull()

'''
    The column "peak-rpm" has 2 empty colmns
    replace it by mean
'''
df["peak-rpm"].replace(np.nan,df["peak-rpm"].astype("float").mean(axis=0),inplace=True)
checknull()
'''
    The price has totally 4 empty values.
    we drop the price rows where the empty values present.
    Because the price is the main factor of all the features in the datasets
    
'''
df.dropna(subset=["price"],inplace=True)
df.reset_index(drop=True,inplace=True)
checknull()
print(df.dtypes)
'''
    Now we need to do the data format .
    firstly check all the columns are in apporiate datatype or not.
    If not Change it to apporiate Datatype.
    
'''
# we can change the datatypes of multiple columns at a time by using list [[]]
df[["bore", "stroke","price","peak-rpm"]] = df[["bore", "stroke","price","peak-rpm"]].astype("float")
df[["normalized-losses"]] = df[["normalized-losses"]].astype("int")
print(df.dtypes)
df["city-L/100KM"]=235/df["city-mpg"]
df.drop("city-mpg",axis=1,inplace=True)
#   We change the data from one form to anothe form and delete the old name
print(df.iloc[3])
df["highway-mpg"]=235/df["highway-mpg"]
df.rename(columns={"highway-mpg":"highway-L/100KM"},inplace=True)
print(df.iloc[4])

''' 
    Now move to Normilization step
    we choose the sample-feature-selection
'''
df["length"]=df["length"]/df["length"].max()
df["width"]=df["width"]/df["width"].max()
df["height"]=df["height"]/df["height"].max()
print(df.iloc[4])

'''
    Now its time for implement the binning
    Binning is used to make the data in ranges.
    pd.cut() method is useful to do binning.
'''
print(df["horsepower"])
df["horsepower"]=df["horsepower"].astype("int")
plt.hist(df["horsepower"])
plt.show()
bins = np.linspace(df["horsepower"].min(),df["horsepower"].max(),4)
groups_names=["LOW","MEDIUM","HIGH"]
df["horsepower_binned"]=pd.cut(df["horsepower"],bins,labels=groups_names,include_lowest=True)
print(df[["horsepower","horsepower_binned"]])
print(df[df["horsepower_binned"]=="HIGH"])
print(df["horsepower_binned"].value_counts().idxmax())
plt.bar(groups_names,df["horsepower_binned"].value_counts())
plt.show()
plt.hist(df["horsepower"],bins=3) #by using the option bins we can identify the the midrange values
plt.show()
print(df.iloc[2])
print(df["fuel-type"].value_counts())
'''
    Now there is a colum called "fuel-type"
    it contains the values of gas and diesel
    so while applying to the model the model didnt understant the 
    categorical values it understand the numerical values.
    so, we can change it to numerical using get_dummies() method
    This method assign 1 if the value is present that row else 0
    
'''
getdummi=pd.get_dummies(df["fuel-type"])
print(getdummi)
df=pd.concat([df,getdummi],axis=1)
print(df.iloc[4])
print(df["aspiration"].value_counts())
indicator=pd.get_dummies(df["aspiration"])
df=pd.concat([df,indicator],axis=1)
print(df.iloc[4])
df.drop("fuel-type",axis=1,inplace=True)
df.drop("aspiration",axis=1,inplace=True)
print(df.iloc[3])

#   Finally we can save the new csv file for further processes like evaluating the models.
df.to_csv("cleanCar.csv")