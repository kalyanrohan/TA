import csv
import pandas as pd
import matplotlib.pyplot as plt
import random as rand

df=pd.read_csv('activity.csv')
# df.dropna(inplace=True)

def get_steps_per_day(df):
    steps_per_day = df.groupby('date').sum()['steps']
    return steps_per_day

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
    mean_per_day=df.groupby('date').mean()['steps']
    return mean_per_day

print('MEAN')
print(get_mean_of_steps_per_day(df))
print('MEDIAN')
def get_median_of_total_steps_per_day(df):
    mean_per_day=df.groupby('date').median()['steps']
    return mean_per_day

#time series plot of the 5-minute interval (x-axis) and the average number of steps taken, averaged across all days (y-axis)
def plot_mean_of_total_steps_per_day():
    plt.plot(get_mean_of_steps_per_day(df))
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
for i in range(len(df)):
    if df['WEEKDAY'][i]<5:
        weekdays.append(df['date'][i])
    else:
        weekends.append(df['date'][i])

print('WEEKDAY')
print(weekdays)

print('WEEKENDS')
print(weekends)

# def plot_average_number_of_steps_across_all_weekdays_and_weekends(df):
#     if df
#     plt.xlabel('5-minute Interval')
#     plt.ylabel('Mean Steps Per Week')
#     plt.title('Mean of Total Steps Per Week')
#     plt.show()
    #plot_average_number_of_steps_across_all_weekdays_and_weekends(df)