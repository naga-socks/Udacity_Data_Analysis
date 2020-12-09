'''
Jhonatan Nagasako
Udacity Data Analysis
Project 1 - Analyzing Global Temps
Purpose:
     Using code and CSV files provide to determine
     moving averages and line graph comparisons

OPPERTUNITY FOR IMPROVEMENT
1. Test scripts
2. Data cleaning (pre-cleaned the docs using excel)

'''
############################
from IPython.display import display
import pandas as pd

# get csv files from github
df_city_data = pd.read_csv("https://raw.githubusercontent.com/naga-socks/Udacity_Data_Analysis/main/Project%201_Explore%20Weather%20Trends/city_data.csv", encoding='utf-8')
df_city_list = pd.read_csv("https://raw.githubusercontent.com/naga-socks/Udacity_Data_Analysis/main/Project%201_Explore%20Weather%20Trends/city_list.csv", encoding='utf-8')
df_global_data = pd.read_csv("https://raw.githubusercontent.com/naga-socks/Udacity_Data_Analysis/main/Project%201_Explore%20Weather%20Trends/global_data.csv", encoding='utf-8')


# Verify head and size
'''
# Check head and size
print("\nData Import Complete - CITY Data")
print(df_city_data.head())
print(df_city_data.info())

print("\nData Import Complete - City NAMES Data")
print(df_city_list.head())
print(df_city_list.info())

print("\nData Import Complete - GLOBAL Data")
print(df_global_data.head())
print(df_global_data.info())
'''

# Remove all NaN from data and only target TOKYO

df_city_data_clean = df_city_data.dropna()
df_city_data_clean.drop('country', axis=1, inplace=True)
#df_city_data_clean.drop(df_city_data_clean.index[0:63891], axis=0, inplace=True)
#df_city_data_clean.drop(df_city_data_clean.index[64061:70793], axis=0, inplace=True)
print(pd.DataFrame(df_city_data_clean))

print(df_city_data_clean.style)

#print(df_city_data_clean.head())

#print("\n", df_global_data.head())

#print(df_city_data_clean.city.unique())

# brute force... drop all but Tokyo
#df_tokyo = df_city_data_clean.drop([Abidjan], axis=0, inplace=True)




#print(df_tokyo.head())

#print() # get names of all rows, remove tokyo, then drop function (same with global data)

# df_tokyo_data_tokyo = df_city_data_clean.drop(')

# df_tokyo_data.drop(columns=['city','country'])

# Verify the length of removed fields
'''
print("\n\nData Import Complete - CITY Data - CLEANED")
print("Before cleaning, ", len(data_city_data))
print("After cleaning, ", len(data_city_data_clean))
'''

#print(data_city_data_clean.head())


# create plots
'''
# import matplotlib.pyplot as plt
import matplotlib.pyplot as plt

# matplotlib inline
plt.style.use('seaborn')

# line plot - the yearly average air temperature in Barcelona
data_city_data_clean.plot(color='green', linewidth=3, figsize=(12,6))

# modify ticks size
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.legend('')

# title and labels
plt.title('The average city temperature', fontsize=20)
plt.xlabel('Year', fontsize=16)
plt.ylabel('Temperature [°C]', fontsize=16)

plt.show()
'''




'''
# calculate the yearly average temp
data_city_data_clean['average_city_data'] = data_city_data_clean.mean(axis=0)
print(data_city_data_clean.head())
print(data_city_data_clean.info())
'''

# Next steps - TEST SCRIPTS
# test if loaded the correct CSV