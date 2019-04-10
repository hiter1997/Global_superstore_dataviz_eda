import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
%matplotlib inline 
import seaborn as sns
import datetime
import scipy.stats as stats


# Reading data:
orders = pd.read_csv("orders.csv")

# checking the scale of the dataset
print("orders dataset contains", orders.shape[0], "rows and", orders.shape[1], "columns.")
orders.head()
print(orders.columns)
print(orders.info())
orders.describe()

print orders['Postal Code'].isnull()


#checking the number of unique customers 
customer_numbers = orders["Customer Name"].nunique()
print("Number of unique customers:",customer_numbers)


states = orders["State"].nunique()
print (states)

countries = orders["Country"].nunique()
print(countries)
regions = orders["Region"].nunique()
print (regions)

sub_categories = orders["Sub-Category"].nunique()
print(sub_categories)
markets = orders["Market"].nunique()
print(markets)
#checking the top cities
cities = orders["City"].nunique()
c1 = orders.groupby('City')['Customer Name'].nunique().sort_values(ascending=False)
print("There are",cities,"unique cities in the dataset. The TOP 10 cities are:")
c2 = c1.head(10)
print(c2)
print("\nTOP 10 cities covers", round(c2.sum()/orders.shape[0]*100,1),"percent of all the orders.")
plt.figure(figsize=(16,8))
c2.plot(kind="bar",rot=0)




