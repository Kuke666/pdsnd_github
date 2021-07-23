import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

MONTHS = ['all','january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']

DAYS = ['all','monday', 'monday', 'tuesday', 'wednesday', 'friday', 'saturday', 'sunday']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city_name = input("Please input name of city you want to explore (chicago, new york city, washington)")
        if city_name.lower() in CITY_DATA:
            city_file = CITY_DATA[city_name.lower()]
            break
        else:
            print("You entered wrong city name, please choose from: chicago, new york city, washington")

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month_name = input("Please choose month, you can choose all or specify(january, february ...)")
        if month_name.lower() in MONTHS:
            month = month_name.lower()
            break
        else:
            print("You entered wrong month name, please choose from: january, february, march...")

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day_name = input("Please choose day, you can choose all or specify(monday, tuesday ...)")
        if day_name.lower() in DAYS:
            day = day_name.lower()
            break
        else:
            print("You entered wrong day name, please choose from: monday, tuesday, wendesday...")


    print('-'*40)
    return city_file, month, day


def load_data(city_file, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(city_file)
    
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.weekday_name

    if month != 'all':
        month = MONTHS.index(month) + 1

        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day'] == day.title()]


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month 
    most_common_month = df['month'].mode()[0]
    print('The most common month for bike leases was: {}'.format(MONTHS[int(most_common_month)]))

    # TO DO: display the most common day of week
    most_common_day = df['day'].mode()[0]
    print(most_common_day)
    print('The most common day for bike leases was: {}'.format(most_common_day))

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    most_common_hour = df['hour'].mode()[0]
    print('The most common day for bike leases was: {}. hour'.format(most_common_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_start_station = df['Start Station'].mode()[0]
    print('The most common starting station was: {}'.format(most_common_start_station))

    # TO DO: display most commonly used end station
    most_common_end_station = df['End Station'].mode()[0]
    print('The most common starting station was: {}'.format(most_common_end_station))

    # TO DO: display most frequent combination of start station and end station trip
    df['trip'] = df['Start Station'] +'--' +  df['End Station']
    most_common_trip = df['trip'].mode()[0]
    print('The most common trip was: {}'.format(most_common_trip))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    travel_time = df['Trip Duration'].sum()
    print('The total trip duration was: {}'.format(travel_time))
    
    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('The mean travel duration was: {}'.format(mean_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city_file):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    counts_user_types = df['User Type'].value_counts()
    print('The value count of user types is: {}'.format(counts_user_types))
    
    city = city_file.split('.')[0]
    if city != 'washington':
       # TO DO: Display counts of gender
       gender_count = df['Gender'].value_counts()
       print('The gender count is: {}'.format(gender_count))

       # TO DO: Display earliest, most recent, and most common year of birth
       earliest_birthdate = df['Birth Year'].min()
       latest_birthdate = df['Birth Year'].max()
       most_common_birthdate = df['Birth Year'].mode()[0]
       print('The most recent birthdate is {}, earliest is {} and most common is {}'.format(latest_birthdate, earliest_birthdate, most_common_birthdate))
    else:
        print("City Washington does not provide gender and birthdate columns, hence wont be displayed")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def process_raw_data(df, counter):
          print(df.iloc[counter:(counter+5), :])
          

def main():
    while True:
        city_file, month, day = get_filters()
        df = load_data(city_file, month, day)
        while True:
           task = input('Would you like to display raw data or filter them? Write either filter or raw. Or if you want exit, write exit.\n')
           if task.lower() == 'filter':
               time_stats(df)
               station_stats(df)
               trip_duration_stats(df)
               user_stats(df, city_file)
               break
           elif task.lower() == 'raw':
               counter = 0
               while True:
                  process_raw_data(df, counter)      
                  loop = input("do you wish to print another 5 rows? Enter yes or no: ")
                  if loop.lower() == 'no': break
                  else: counter+=5
           elif task.lower() == 'exit':
               break
           else:
               print('The input you gave is wrong, please try again')

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
