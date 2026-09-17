import time
import pandas as pd

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

    # get user input for city (chicago, new york city, washington)
    selected_city = input("\nPlease type ch if you would you like to see data for Chicago, ny for New York City or w for Washington?\n").lower()
    while selected_city not in {'ch','ny','w'}:
        print('That isn\'t a valid city name\n')
        selected_city = input("\nPlease type ch if you would you like to see data for Chicago, ny for New York City or w for Washington?\n").lower()
    if selected_city == 'ch':
        city = "chicago"
        print("\nLooks like you want to hear about {}!  If this is not true, restart the program now!".format(city.title()))
    elif selected_city == 'ny':
        city = "new york city"
        print("\nLooks like you want to hear about {}!  If this is not true, restart the program now!".format(city.title()))
    elif selected_city == "w":
        city = "washington"
        print("\nLooks like you want to hear about {}!  If this is not true, restart the program now!".format(city.title()))


    # get user input for month
    data_filteration = input("\nWould you like to filter the data by month, day, both or not at all? Type (none) for no time filter.\n").lower()

    # Handling invalid inputs from the user
    while data_filteration not in {'month','day','both','none'}:
        print('That isn\'t a valid input\n')
        data_filteration = input("\nWould you like to filter the data by month, day, both or not at all? Type (none) for no time filter.\n").lower()

    months_list = ['january', 'february', 'march', 'april', 'may', 'june']
    days_list = ['saturday', 'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday']

    if data_filteration == 'month':
        selected_month = input("\nWhich month? January, February, March, April, May or June?\n").lower()
        while selected_month not in months_list:
            print("That\'s not a valid input, please type again\n")
            selected_month = input("\nWhich month? January, February, March, April, May or June?\n").lower()

        month = selected_month
        day = 'all'

    # get user input for day of week (all, monday, tuesday, ... sunday)

    elif data_filteration == 'day':
        selected_day = input("\nWhich day? Saturday, Sunday, Monday, Tuesday, Wednesday, Thursday, Friday\n").lower()
        while selected_day not in days_list:
            print("That\'s not a valid input, please type again\n")
            selected_day = input("\nWhich day? Saturday, Sunday, Monday, Tuesday, Wednesday, Thursday, Friday\n").lower()

        day = selected_day
        month = "all"

    elif data_filteration == 'both':
            selected_month = input("\nWhich month? January, February, March, April, May or June?\n").lower()
            while selected_month not in months_list:
                print("That\'s not a valid input, please type again\n")
                selected_month = input("\nWhich month? January, February, March, April, May or June?\n").lower()

            month = selected_month

            selected_day = input("\nWhich day? Saturday, Sunday, Monday, Tuesday, Wednesday, Thursday, Friday\n").lower()
            while selected_day not in days_list:
                print("That\'s not a valid input, please type again\n")
                selected_day = input("\nWhich day? Saturday, Sunday, Monday, Tuesday, Wednesday, Thursday, Friday\n").lower()

            day = selected_day


    elif data_filteration == 'none':
        print('\nGathering data for the first 6 months.\n')
        month = 'all'
        day = 'all'



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
    # loading the dataset for the specified city into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # Create month and day_of_week columns while importing as names for easy filtering
    df['month'] = df['Start Time'].dt.month_name()
    df['day_of_week'] = df['Start Time'].dt.day_name()

    # filter by month if applicable
    if month != 'all':
        # filter by month to create the new dataframe
        df = df[df['month'] == month.title()]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        # capitalize the day parameter to match the title case as in its dataframe column
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df, month="all", day="all"):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    if month == 'all':
        most_common_month = df['month'].mode()[0]
        print("Most Common Month: ", most_common_month.title())

    # display the most common day of week
    if day == 'all':
        most_common_weekday = df['day_of_week'].mode()[0]
        print("Most Common Day of Week: ", most_common_weekday)

   # Create hour column from the Start Time column
    df['hour'] = df['Start Time'].dt.hour

    # display the most common start hour
    popular_hour = df['hour'].mode()[0]
    print('Most Frequent Start Hour:', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...')
    start_time = time.time()

    # display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print('\nMost commonly used start station: ', common_start_station)

    # display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print('\nMost commonly used end station: ', common_end_station)



    # display most frequent combination of start station and end station trip
        # create a new column to add the start and end stations in one dataframe to apply filtering
    df['route'] = df['Start Station'] + " --- " + df['End Station']

        # display the most frequent trip
    most_freq_trip = df['route'].mode()[0]
    print('\nMost commonly used trip: ', most_freq_trip)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
        # create a dataframe for total travel time from the Trip Duration coulmn
    total_time = df['Trip Duration'].sum()

        # convert the total time in seconds to days, hours, minutes & seconds for an elegant display
    days = total_time // (24 * 3600)
    total_time %= (24 * 3600)
    hours = total_time // 3600
    total_time %= 3600
    minutes = total_time // 60
    total_time %= 60
    print("Total travel time in (d:h:m:s): ", '%d:%d:%d:%d' % (days, hours, minutes, total_time))


    # display mean travel time
        # create a dataframe for average travel time from the Trip Duration coulmn
    mean_time = df['Trip Duration'].mean()

        # convert the total time in seconds to days, hours, minutes & seconds for an elegant display
    days = mean_time // (24 * 3600)
    mean_time %= (24 * 3600)
    hours = mean_time // 3600
    mean_time %= 3600
    minutes = mean_time // 60
    mean_time %= 60
    print("Mean travel time in (d:h:m:s): ", '%d:%d:%d:%d' % (days, hours, minutes, mean_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    users_count = df['User Type'].value_counts().to_string()
    print("Breakdown of users:")
    print(users_count)


    # Display counts of gender
    print("\nCalculating the next statistic... Gender\n")
    if 'Gender' in df:
        gender_count = df['Gender'].value_counts().to_string()
        print("Count of users gender:")
        print(gender_count)
    else:
        print("No (Gender) data for this city to share")

    # Display earliest, most recent, and most common year of birth
    print("\nCalculating the next statistic...year of birth\n")

    if 'Birth Year' in df:
        earliest_year = df['Birth Year'].min()
        most_recent_year = df['Birth Year'].max()
        most_common_year = df['Birth Year'].mode()[0]
        print("Earliest year of birth: ", int(earliest_year))
        print("Most recent year of birth: ", int(most_recent_year))
        print("Most common year of birth: ", int(most_common_year))
    else:
        print("No (Birth Year) data for this city to share")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def display_raw_data(city):
    """
    Asks the user if he wants to display another 5 rows of data for the specified city.

    Args:
        (str) city - name of the city returned by the get_filters function

    Returns:
        chunks of 5 rows of data for the specified city
    """
    # import our dataframe
    df = pd.read_csv(CITY_DATA[city])
    row_num = 0
    # validate the user answer for whether he wants to display raw data or not
    while True:
        view_data = input("Type yes if you would like to view more raw data in 5 row chunks or no if you want to exit\n").lower()
        if view_data not in ['yes', 'no']:
            print("Invalid input, please type yes or no")

        elif view_data == 'yes':
            print(df.iloc[row_num:row_num+5])
            row_num += 5

        elif view_data == 'no':
            print("\nExiting the program...")
            break





def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        if df.empty:
            print("No trips match the selected filters.")
        else:
            time_stats(df, month, day)
            station_stats(df)
            trip_duration_stats(df)
            user_stats(df)
            display_raw_data(city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            print("\nThank you")
            break


if __name__ == "__main__":
    main()
