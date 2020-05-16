import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

#making the first change in this file to pass in udacity review              

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('\nHello! Let\'s explore some US bikeshare data!')

    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    cities = ('chicago', 'new york city', 'washington')
    while True:
        city = input('\nPlease select the city from the city below for which you want to see data \nChicago \nNew York City \nWashington\n').lower()
        if city not in cities:
            print('\nInvalid entry, please select the city from the specified entires above and try again.')
            continue
        else:
            break


    # TO DO: get user input for month (all, january, february, ... , june)
    months = ('all', 'january', 'february', 'march', 'april', 'may', 'june', 'jan', 'feb', 'mar', 'apr', 'may', 'jun')
    while True:
        month = input('\nPlease select the month between January to June (both inclusive) from which you want to filter the data, select All if you want to filter out data for all the months\nJanuary \nFebruary \nMarch \nApril \nMay \nJune \nAll\n').lower()
        if month not in months:
            print('Invalid entry, please select the month from the specified entires above and try again.')
            continue
        else:
            if month == 'jan':
                month = months[1]
            if month == 'feb':
                month = months[2]
            if month == 'mar':
                month = months[3]
            if month == 'apr':
                month = months[4]
            if month == 'may':
                month = months[5]
            if month == 'jun':
                month = months[6]
            break


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days = ('all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun')
    while True:
        day = input('\nPlease select the day by which you want to filter the data, select All if you want to filter out data for all days \nMonday \nTuesday \nWednesday \nThursday \nFriday \nSaturday \nSunday \nAll \n').lower()
        if day not in days:
            print('Invalid entry, please select the day from the specified entires above and try again.')
            continue
        else:
            if day == 'mon':
                day = days[1]
            if day == 'tue':
                day = days[2]
            if day == 'wed':
                day = days[3]
            if day == 'thu':
                day = days[4]
            if day == 'fri':
                day = days[5]
            if day == 'sat':
                day = days[6]
            if day == 'sun':
                day = days[7]
            break


    print('-'*50)
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
    df = pd.read_csv(CITY_DATA[city]) 
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour
    df['End Time'] = pd.to_datetime(df['End Time'])
    df['month'] = df['End Time'].dt.month
    df['day_of_week'] = df['End Time'].dt.day_name()
    df['hour'] = df['End Time'].dt.hour

    # filters by month 
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]

    # filters by day 
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_common_month = df['month'].mode()[0]
    print('Most common month: ', most_common_month)

    '''In the abpve lines of code using df['month'] we are fetching the column month from the data frame and using the mode()
    function we are fetching the most frequetly occurred value in months, [0] is used to fetch values column-wise
    [1] can be used to fetch values row-wise. Similarly we can calculate most common day of the week and most common 
    start hour.'''

    # TO DO: display the most common day of week
    most_common_day_of_week = df['day_of_week'].mode()[0]
    print('Most common day of week: ', most_common_day_of_week)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    most_common_start_hour = df['hour'].mode()[0]
    print('Most common hour: ', most_common_start_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*50)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_start_stn = df['Start Station'].mode()[0]
    print('Most commonly used start station: ', most_common_start_stn)

    # TO DO: display most commonly used end station
    most_common_end_stn = df['End Station'].mode()[0]
    print('Most commonly used end station: ', most_common_end_stn)

    # TO DO: display most frequent combination of start station and end station trip
    df['Most frequent station combo'] = df['Start Station'] + ' to ' + df['End Station']
    most_freq_trip = df['Most frequent station combo'].mode()[0]
    print('Most frequent combination of start station and end station: ', most_freq_trip)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*50)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('Total travel time: ', total_travel_time)

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('Mean travel time: ',mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*50)

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type = df['User Type'].value_counts()
    print('User type counr: ', user_type)

    '''the method value_counts() returns the number of unique values in the decending order with the first element
    in the order being the most frequently occuring element'''

    # TO DO: Display counts of gender
    try:
        gender_count = df['Gender'].value_counts()
        print('Gender count: ', gender_count)
    except KeyError:
        print('No data available in Gender for the selected filters. You may try with diffrent combination of filters.')

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest_yob = int(df['Birth Year'].min())
        print('Earliest year of birth: ', earliest_yob)
    except KeyError:
        print('No data available in Earliest year of birth for the selected filters. You may try with diffrent combination of filters.')
    try:
        recent_yob = int(df['Birth Year'].max())
        print('Most recent year of birth: ', recent_yob)
    except KeyError:
        print('No data available in Most recent year of birth for the selected filters. You may try with diffrent combination of filters.')
    try:
        most_common_yob = int(df['Birth Year'].mode()[0])
        print('Most common year of birth: ', most_common_yob)
    except KeyError:
        print('No data available in Most common year of birth for the selected filters. You may try with diffrent combination of filters.')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*50)
    
def display_data(df):
    disp_data = input("Would you like to see 5 rows of raw data? Yes/No :").lower()
    if disp_data != 'no':
        i=0
        while(i<df['Start Time'].count() and disp_data != 'no'):
            print(df.iloc[i:1+5])
            i = i + 5
            more_data = input('\nWould you like to see 5 more rows of data? Yes/No: ').lower()
            if more_data != 'yes':
                break

def main():
    while True:
        city, month, day = get_filters()

        while True:
            print('City: ', city.title(), '\nMonth: ', month.title(), '\nDay: ', day.title()) 
            decision = input('Kindly confirm the city, month and day filters for the analysis of data. If you want to change any of the filters \nEnter "change" else enter "continue" to continue with the selected filters.\n')
            if decision.lower() == 'change':
                city, month, day = get_filters()
            elif decision.lower() == 'continue':
                break

        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()