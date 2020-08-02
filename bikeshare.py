import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
# TO DO: get user input for city (chicago, new york city, washington).
# HINT: Use a while loop to handle invalid inputs
    
    input_city = input('Please choose one of these cities: Chicago, New York City, Washington \n').lower()
    while input_city not in ['chicago', 'new york city', 'washington']:
    print("I'm not sure what city you are referring to. Please try again!")
    input_city = input('Please choose one of these cities: Chicago, New York City, Washington \n').lower()
    city = CITY_DATA[input_city]

# TO DO: get user input for month (all, january, february, ... , june)
    month = input('Please enter the month - January, February, March, April, May or June \n').title()
    while month not in ['January', 'February', 'March', 'April', 'May', 'June']:
    print("I'm not sure what month you're referring to. Please try again!")

month = input('Please enter the month or ALL \n').title()
if month == 'January':
month == '01'
elif month == 'February':
month == '02'
elif month == 'March':
month == '03'
elif month == 'April':
month == '04'
elif month == 'May':
month == '05'
elif month == 'June':
month == '06'
else:
print("I'm not sure what month you're referring to. Please try again!")
month = input('Please enter the month or ALL \n').title()


# TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
day_of_week = input('Please input the day of the week \n').title()
while day_of_week not in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']:
print("I'm not sure what day you're referring to. Please try again!")
day_of_week = input('Please input the day of the week or ALL \n').title()
if day_of_week == 'Monday':
day_of_week == 0
elif day_of_week == 'Tuesday':
day_of_week == 1
elif day_of_week == 'Wednesday':
day_of_week == 2
elif day_of_week == 'Thursday':
day_of_week == 3
elif day_of_week == 'Friday':
day_of_week == 4
elif day_of_week == 'Saturday':
day_of_week == 5
elif day_of_week == 'Sunday':
day_of_week == 6
else:
print("I'm not sure what day you're referring to. Please try again!")
day_of_week = input('Please input the day of the week or ALL \n').title()

print('-'*40)
return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
# Load file in dataframe
filename = ('{}.csv'.format(city))
df = pd.read_csv(filename)

# Convert Start Time data to Date time
df['Start Time'] = pd.to_datetime(df['Start Time'])

# Extract month and day of week from Start Time
df['month'] = df['Start Time'].dt.month
df['day_of_week'] = df['Start Time'].dt.weekday_name

# Filter by month if applicable
# Use index of months to get corresponding list
if month != 'all':
months = ['January', 'February', 'March', 'April', 'May', 'June']
month = months.index(month) + 1

# Filter by month to create new dataframe
df = df[df['month'] == month]

# Filter day of week if applicable
if day != 'all':

# Filter by day of week to create new dataframe
df = df[df['day_of_week'] == day.title()]

return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

# TO DO: display the most common month

# Convert Start Time data to Date time
df['Start Time'] = pd.to_datetime(df['Start Time'])
df['month'] = df['Start Time'].dt.month
common_month = df['month'].mode()[0]
print('The most common month traveled: {}.\n'.format(common_month))

# TO DO: display the most common day of week
df['day_of_week'] = df['Start Time'].dt.weekday_name
common_day_of_week = df['day_of_week'].mode()[0]
print('The most common day of the week traveled: {}.\n'.format(common_day_of_week))

# TO DO: display the most common start hour
df['Start Time'] = pd.to_datetime(df['Start Time'])
df['hour'] = df['Start Time'].dt.hour
common_hour = df['hour'].mode()[0]
print('The most common hour traveled: {}.\n'.format(common_hour))


print("\nThis took %s seconds." % (time.time() - start_time))
print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

# TO DO: display most commonly used start station
    count_start_station = df.groupby(['Start Station']).size().sort_values(ascending=False).index[0]
    print('The most common start station: {}.\n'.format(count_start_station))

# TO DO: display most commonly used end station
    counts_end_station = df.groupby(['End Station']).size().sort_values(ascending = False).index[0]
    print('The most common End Station: {}.\n'.format(counts_end_station))

# TO DO: display most frequent combination of start station and end station trip
    popular_station_combination = df.groupby(['Start Station', 'End Station']).size().nlargest(1)
    print('The most common start and end station combination: {}.\n'.format(popular_station_combination))

print("\nThis took %s seconds." % (time.time() - start_time))
print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

# TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum() / 60 / 60 / 24
    return[total_travel_time]

# TO DO: display mean travel time
    avg_travel_time = df['Trip Duration'].mean / 60
    return[avg_travel_time]

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

# TO DO: Display counts of user types
    user_types = df['User_Type'].value_counts()
    print(user_types)

# TO DO: Display counts of gender
    gender_count = df['Gender'].value_counts()
    print('The gender count is: ', gender_count)
    
# TO DO: Display earliest, most recent, and most common year of birth
    earliest_year = df['Birth Year'].min()
    print('The earliest birth year: {}.\n'.format(earliest_year))
    latest_year = df['Birth Year'].max()
    print('The latest birth year: {}.\n'.format(latest_year))
    common_year = df['Birth Year'].mode()
    print('The most common birth year: {}.\n'.format(common_year))
except:
    print('Gender or birth year column is not available for washington')
    
     print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
# TO DO: Displays raw data
def raw_data(df):
    i = 0
    raw = ('\nWould you like to view the first 5 rows of raw data? Enter yes or no.\n').lower()
    pd.set_option('display.max_columns', 200)
    while True:
        print(df.iloc[0:5])
        i += 5
        raw = input("Do you wish to view next rows of raw data?: ").lower()
    if raw == 'no':
        break
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break
            
if __name__ == "__main__":
	main()
   