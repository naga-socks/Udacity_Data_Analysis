'''
Jhonatan Nagasako
Udacity Data Analysis
Project 1 - Analyzing Global Temps
Purpose:
     Using code and CSV files provide to determine
     moving averages and line graph comparisons

OPPORTUNITY FOR IMPROVEMENT
1. Test scripts
2. Data cleaning (pre-cleaned the docs using excel)

HELP WITH CODING PROJECT IN PYTHON
# project help in PYTHON --> https://towardsdatascience.com/moving-averages-in-python-16170e20f6c
# doing the data analysis in EXCEL would have been EASY -- it was more of a challenge programming in PYTHON!

HELP WITH PLOTTING
# plotting help --> https://swcarpentry.github.io/python-novice-gapminder/09-plotting/
# subplot help --> https://bertvandenbroucke.netlify.app/2019/07/10/the-many-ways-to-combine-plots-in-python/
# HELP WITH PLOT AXIS CONTROL --> https://www.kite.com/python/docs/matplotlib.pyplot.xlim

HELP WITH SQL
# BETWEEN function --> https://www.w3schools.com/sql/sql_between.asp
# WHERE function --> https://www.w3schools.com/sql/sql_where.asp
'''
############################
from IPython.display import display
import pandas as pd

# get csv files from github
df_global_data = pd.read_csv("https://raw.githubusercontent.com/naga-socks/Udacity_Data_Analysis/main/Project%201_Explore%20Weather%20Trends/short_global_data.csv", encoding='utf-8')
df_japan = pd.read_csv("https://raw.githubusercontent.com/naga-socks/Udacity_Data_Analysis/main/Project%201_Explore%20Weather%20Trends/tokyo_city_data.csv",encoding='utf-8')

# Verify head and size
print("\nData Import Complete - TOKYO Data")
print(df_japan.head())
print("---------------------")
print(df_japan.info())

print("\nData Import Complete - GLOBAL Data")
print(df_global_data.head())
print("---------------------")
print(df_global_data.info())

print("=========================================")
print("===========minimum data clean============")
print("=========================================")
# Remove all NaN from data that will be analyzed also minimum data cleaning
df_japan.dropna()
print(df_japan.head()) #checking that the city column removed from Japan data

df_global_data.dropna()


print("=========================================")
print("===========average temps============")
print("=========================================")

# set year as index
df_japan.set_index('year', inplace=True)
df_japan.index.name = 'year'
df_japan['japan_average_temperature'] = df_japan.mean(axis=1)
df_japan = df_japan[['japan_average_temperature']]
print(df_japan.head()) # check work

df_global_data.set_index('year', inplace=True)
df_global_data.index.name = 'year'
df_global_data['global_average_temperature'] = df_global_data.mean(axis=1)
df_global_data = df_global_data[['global_average_temperature']]
print(df_global_data.head()) # check work

print("=========================================")
print("===========create plots============")
print("=========================================")

# plotting help --> https://swcarpentry.github.io/python-novice-gapminder/09-plotting/

# create plots
import matplotlib.pyplot as plt

# matplotlib inline
plt.style.use('bmh')

print("=========================================")
print("===========SIMPLE moving average plots============")
print("=========================================")

# SIMPLE moving average = SMA of 10 years
df_japan['SMA_10'] = df_japan.japan_average_temperature.rolling(10, min_periods=1).mean()
df_global_data['SMA_10'] = df_global_data.global_average_temperature.rolling(10, min_periods=1).mean()

#JAPAN TEMP SMA
# colors for the line plot
colors = ['green', 'orange']

# line plot - the yearly average japan temp
df_japan[['japan_average_temperature', 'SMA_10']].plot(color=colors, linewidth=3, figsize=(12,6))

# modify ticks size
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.legend(labels =['Average Temp', 'SMA_10'], fontsize=14)

# range axis control
# HELP WITH PLOT AXIS CONTROL --> https://www.kite.com/python/docs/matplotlib.pyplot.xlim
plt.ylim(7.5, 16.5)

# title and labels
plt.title('Yearly Average Temp of TOKYO, Japan', fontsize=20)
plt.xlabel('Year', fontsize=16)
plt.ylabel('Temperature [°C]', fontsize=16)

#-------------------------------
# GLOBAL TEMP SMA
# colors for the line plot
colors = ['steelblue', 'deeppink']

# line plot - the yearly accumulated global temp
df_global_data[['global_average_temperature', 'SMA_10']].plot(color=colors, linewidth=3, figsize=(12,6))

# modify ticks size
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.legend(labels =['Average Temp', 'SMA_10'], fontsize=14)

# range axis control
plt.ylim(7.5, 16.5)

# title and labels
plt.title('Yearly Average Temp of Globe', fontsize=20)
plt.xlabel('Year', fontsize=16)
plt.ylabel('Temperature [°C]', fontsize=16)


# =========== COMBINE BOTH PLOTS =========================
# subplot help: https://bertvandenbroucke.netlify.app/2019/07/10/the-many-ways-to-combine-plots-in-python/

fig, ax = plt.subplots(2, 1)

ax[0].plot(df_japan)
ax[1].plot(df_global_data)
# range axis control
plt.ylim(7.5, 16.5)

plt.show()
