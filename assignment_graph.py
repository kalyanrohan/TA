import csv
import pandas as pd
import matplotlib.pyplot as plt
import random as rand

df=pd.read_csv('activity.csv')
print(df.info())
# df.dropna(inplace=True)

def get_steps_per_day(df):
    steps_per_day = df.groupby('date', dropna=True).sum()['steps']
    return steps_per_day.to_frame()

print('steps_per_day')
print(get_steps_per_day(df))

def histogram_of_total_steps_per_day(df):
    steps_per_day = get_steps_per_day(df)
    plt.hist(steps_per_day)
    plt.xlabel('Total Steps')
    plt.ylabel('Days')
    plt.title('Histogram of Total Steps Per Day')
    plt.show()

histogram_of_total_steps_per_day(df)

def get_mean_of_steps_per_day(df):
    mean_per_day=df.groupby('date', dropna=True).mean()['steps']
    return mean_per_day.to_frame().dropna()

print('MEAN')
print(get_mean_of_steps_per_day(df))
def get_median_of_total_steps_per_day(df):
    mean_per_day=df.groupby('date', dropna=True).median()['steps']
    return mean_per_day.to_frame().dropna()

print('MEDIAN')
print(get_median_of_total_steps_per_day(df))

#time series plot of the 5-minute interval (x-axis) and the average number of steps taken, averaged across all days (y-axis)
def plot_mean_of_total_steps_per_day():
    plt.plot(get_mean_of_steps_per_day(df), 'r')
    plt.xlabel('5-minute Interval')
    plt.ylabel('Mean Steps Per Day')
    plt.title('Mean of Total Steps Per Day')
    plt.show()

plot_mean_of_total_steps_per_day()

print('DAY THAT HAS MOST STEPS:')
def get_date_that_have_max_steps_per_5_minute_interval():
    steps_per_day = get_steps_per_day(df)
    return steps_per_day.idxmax()

print(get_date_that_have_max_steps_per_5_minute_interval())

def get_number_of_Nans(df):
    return df.isnull().sum()

print('NUMBER OF NANS:')
print(get_number_of_Nans(df))

def fill_in_Nans_with_random_values_and_create_new_dataset():
    new_dataset =df.copy()
    new_dataset.fillna(rand.randint(0,100), inplace=True)
    return new_dataset

print('\n new_dataset \n')
new_dataset=fill_in_Nans_with_random_values_and_create_new_dataset()
histogram_of_total_steps_per_day(new_dataset)
print('MEAN OF NEW DATASET')
print(get_mean_of_steps_per_day(new_dataset))
print('MEDIAN OF NEW DATASET')
print(get_median_of_total_steps_per_day(new_dataset))

#classify dates to weekend or weekdays
df['WEEKDAY'] = pd.to_datetime(df['date']).dt.dayofweek
weekdays=[]
weekends=[]
weekdays_average_steps=[]
weekends_average_steps=[]
for i in range(len(df)):
    if df['WEEKDAY'][i]<=5 and df['date'][i] not in weekdays:
        weekdays.append(df['date'][i])
    elif df['WEEKDAY'][i]>5 and df['date'][i] not in weekends:
        weekends.append(df['date'][i])

for i in range(len(weekdays)):
    weekdays_average_steps.append(get_mean_of_steps_per_day(df[df['date']==weekdays[i]])['steps'])

for i in range(len(weekends)):
    weekends_average_steps.append(get_mean_of_steps_per_day(df[df['date']==weekends[i]])['steps'])

#plotting the average steps per day for weekdays and weekends
plt.figure(figsize=(20,5), dpi=100)
plt.plot(weekdays, weekdays_average_steps, 'ro')
plt.plot(weekends, weekends_average_steps, 'bo')
plt.xlabel('Date')
plt.ylabel('Average Steps Per Day')
plt.title('Average Steps Per Day for Weekdays and Weekends')
plt.show()