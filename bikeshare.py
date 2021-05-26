import time
import pandas as pd


# Set to Display All Columns
# This is necessary to view all columns when viewing raw data
pd.set_option('display.max_columns', None)

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }


def yes_no(prompt):
    #Validates yes or no prompts
    while True:
        choice = input(prompt + ' Enter yes or no: ')
        if choice.lower() == 'yes':
            return True
        elif choice.lower() == 'no':
            return False
        else:
            print (f'Response {choice} is INVALID! Please tray again: ')


def display_banner():
    # Displays opening banner with greeting based on hour of the day.
    current_hour = time.strptime(time.ctime(time.time())).tm_hour
    if current_hour < 12 :
        greeting = 'Good Morning!'
    elif current_hour >= 12 and current_hour < 18 :
        greeting = "Good Afternoon!"
    elif current_hour >= 18 :
        greeting = 'Good Evening!'
    length_greeting = len(greeting)
    print('-'*(38+length_greeting))
    print(f'{greeting} Let\'s explore some US bikeshare data!')
    print('-'*(38+length_greeting))



def city_menu_choice():
    # Displays city menu choices (saves typing) and validates input
    print ("\nChoose City Menu")
    print ("----------------")
    print ("1) Chicago")
    print ("2) New York City")
    print ("3) Washington")
    while True:
        choice = input('Enter Valid Number for City Choice: ')
        if choice == '1':
            city = 'Chicago'
            break;
        elif choice == '2':
            city = 'New York City'
            break;
        elif choice == '3':
            city = 'Washington'
            break;
        else:
            print(f'City Choice {choice} is INVALID! Please enter 1, 2 or 3: ')
    print(f'Bikeshare City data to explore is: {city}')
    return city.lower()



def month_menu_choice():
    # Displays month filter menu choices (saves typing) and validates input
    print ("\nMonth Filter Menu")
    print ("-----------------")
    print ("1) January")
    print ("2) February")
    print ("3) March")
    print ("4) April")
    print ("5) May")
    print ("6) June")
    print ("0) All\n")
    while True:
        choice = input('Enter Valid Number for Month Filter Choice: ')
        if choice == '1':
            month = 'January'
            break;
        elif choice == '2':
            month = 'February'
            break;
        elif choice == '3':
            month = 'March'
            break;
        if choice == '4':
            month = 'April'
            break;
        elif choice == '5':
            month = 'May'
            break;
        elif choice == '6':
            month = 'June'
            break;
        elif choice == '0':
            month = 'all'
            print('Bikeshare Data Results will include All Months!')
            break;
        else:
            print(f'Month Choice {choice} is INVALID! Please enter 1, 2, 3, 4, 5, 6 or 0: ')
    print(f'Bikeshare Month data to filter is: {month}')
    return month



def day_menu_choice():
    # Displays day filter menu choices (saves typing) and validates input
    print ("\nDay Filter Menu")
    print ("---------------")
    print ("1) Sunday")
    print ("2) Monday")
    print ("3) Tuesday")
    print ("4) Wednesday")
    print ("5) Thursday")
    print ("6) Friday")
    print ("7) Saturday")
    print ("0) All\n")
    while True:
        choice = input('Enter Valid Number for Day Filter Choice: ')
        if choice == '1':
            day = 'Sunday'
            break;
        elif choice == '2':
            day = 'Monday'
            break;
        elif choice == '3':
            day = 'Tuesday'
            break;
        if choice == '4':
            day = 'Wednesday'
            break;
        elif choice == '5':
            day = 'Thursday'
            break;
        elif choice == '6':
            day = 'Friday'
            break;
        elif choice == '7':
            day = 'Saturday'
            break;
        elif choice == '0':
            day = 'all'
            print('Bikeshare Data Results will include All Days!')
            break;
        else:
            print(f'Day Choice {choice} is INVALID! Please enter 1, 2, 3, 4, 5, 6, 7 or 0: ')
    print(f'Bikeshare Day of week data to filter is: {day}')
    return day



def convert_hour(hour_integer):
    #Converts a 24 hour integer into a 12 hour string
    remainder = hour_integer / 12.0
    if remainder < 1.0:
        return str(hour_integer) + ':00 AM'
    elif remainder > 1.0:
        return str(hour_integer % 12) + ':00 PM'
    else:
        return '12:00 PM'



def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    # Obtain user input for city, month and day
    city = city_menu_choice()
    month = month_menu_choice()
    day = day_menu_choice()
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
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # Extract month, day of week and hour from Start Time to create 3 new columns
    # Verified with Spyder Debugging and Variable Explorer
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour
    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['January', 'February', 'March', 'April', 'May', 'June']
        month = months.index(month) + 1
        # filter by month to create the new dataframe
        df = df[df['month'] == month]
    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
    return df



def time_stats(df):
    """Displays statistics on the most common times of travel."""
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    # display the most common month
    months = ['January', 'February', 'March', 'April', 'May', 'June']
    month_mode = df['month'].mode()[0]
    month_mode = months[month_mode-1]
    print(f'The Most Frequent Month: {month_mode}')
    # display the most common day of week
    day_mode = df['day_of_week'].mode()[0]
    print(f'The Most Frequent Day: {day_mode}')
    # display the most common start hour
    hour_mode = df['hour'].mode()[0]
    hour12 = convert_hour(hour_mode)
    print(f'The Most Frequent Hour: {hour_mode} ({hour12})')
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def station_stats(df):
    """Displays statistics on the most popular stations and trip."""
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    # display most commonly used start station
    start_station_mode = df['Start Station'].mode()[0]
    print(f'The Most Popuar Start Station: {start_station_mode}')
    # display most commonly used end station
    end_station_mode = df['Start Station'].mode()[0]
    print(f'The Most Popuar End Station: {end_station_mode}')
    # display most frequent combination of start station and end station trip
    routes = df['Start Station'] + '  TO  ' +  df['End Station']
    route_mode = routes.mode()[0]
    print(f'The Most Popuar Route: {route_mode}')
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    # display total travel time
    trip_duration_sum = round(df['Trip Duration'].sum()/60.0,2)
    print(f'Total Travel Time: {trip_duration_sum} Minutes')
    # display mean travel time
    trip_duration_mean = round(df['Trip Duration'].mean()/60.0,2)
    print(f'Average Trip Duration: {trip_duration_mean} Minutes')
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def user_stats(df):
    """Displays statistics on bikeshare users."""
    print('\nCalculating Bikeshare User Statistics...')
    start_time = time.time()
    # Display counts of user types
    print('\nCounts of User Types:')
    print(df['User Type'].value_counts())
    # Display counts of gender
    print('\nCounts by Gender:')
    #Error Handling code to capture key error if Gender values do not exist
    try:
        #code which gives key error if Gender values do not exist
        df_gender_subset = df.dropna(subset=['Gender'])
        print(df_gender_subset['Gender'].value_counts())
    except KeyError:
        print ('Gender values do not exist in this BikeShare dataset!')
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    # Display earliest, most recent, and most common year of birth
    print('\nCalculating Birth Year Statistics...\n')
    start_time = time.time()
    #code which gives key error if Gender values do not exist
    try:
        df_birthyear_subset = df.dropna(subset=['Birth Year'])
        minvalue = round(df_birthyear_subset['Birth Year'].min())
        print(f'Earliest Birth Year:  {minvalue}')

        maxvalue = round(df_birthyear_subset['Birth Year'].max())
        print(f'Most Recent Birth Year:  {maxvalue}')

        modevalue = round(df_birthyear_subset['Birth Year'].mode()[0])
        print(f'Most Common Birth Year:  {modevalue}')
    except KeyError:
        print ('Birth Year values do not exist in this BikeShare dataset!')
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def view_data_records(df):
    """ Allows user the option to view 5 data records at a time. """
    # Initialize Start Row
    start_row = 0
    #Check if Birth Year column exists to avoid KeyError
    if 'Birth Year' in df.columns:
        df['Birth Year'] = df['Birth Year'].fillna('0')
        df['Birth Year'] = df['Birth Year'].astype(int)
        df['Birth Year'] = df['Birth Year'].replace(0,'')
    response = yes_no('\n\nWould you like to view the first 5 individual trip data records? ')
    while response:
        print('-'*72)
        print("Raw Data:\n{}".format(df[start_row : start_row + 5]))
        print('-'*72)
        start_row += 5
        response = yes_no('\nWould you like to view 5 more individual trip data records? ')



def main():
    while True:
        display_banner()
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        view_data_records(df)
        restart = yes_no('\nWould you like to explore BikeShare data again? ')
        if restart == False:
            break


if __name__ == "__main__":
	main()
