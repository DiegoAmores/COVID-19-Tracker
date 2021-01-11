# Programmers: Kristen Wagner, Chandra Tamang, Minsung Kim, and Diego Amores
import click
import csv
import matplotlib.pyplot as plt
import pandas as pd
import os
import re
import sys

from datetime import date, datetime, timedelta
from covid_information import CovidInfo
from live_covid_information import LiveCovidInfo
from os import path

#FOR MAC USERS ONLY
#import ssl 
#ssl._create_default_https_context = ssl._create_unverified_context


"""
INST 326 Object Oriented Programming Final Project
Group - 107
Prof: Aric Bills
"""

class CovidTrackerApp():
    """
    CovidTrackerApp class has 10 different functions, and all functions have
    different purposes.
    
    add_report()
        This function will ask users to input data for a new COVID report.
        
    read_file()
        This function will import data from data.humdata.org API into our program.
        
    write_file()
        This function will write data from our CovidTrack Application into a 
        CSV file.
        
    get_latest_report()
        This function will retrieve the latest COVID report date.
    
    find_state()
        This function will find the latest information of COVID cases/deaths of a 
        state.
    
    latest_highest_deaths_rates()
        This function will retrieve the latest information of COVID reports and show
        the current total cases, total deaths, and death rates.
    
    recent_most_case_area()
        This function will show the recent cases reported from input date up 
        until current date.
    
    recent_most_death_area()
        This function will show the recent deaths reported from input date up 
        until current date.
    
    covid_cases_data()
        This function will use regular expression to access states and death 
        values and return a tuple of state and deaths.
    
    highest_cases_graph()
        This function will convert a tuple into a dictionary and sort data from states
        with highest number of deaths and displays a plot sorted list bar graph.
        
    Attributes:
        info (set): A set of COVID report objects
        
        report_add (bool): A boolean to check whether or not a new user has inputted
        a new COVID report.
        
        report_counter (int): A counter to count the number of new COVID reports entered.
    
    Side Effect:
        Functions could modify info.
        Prints to stdout.
    """
    info = set()
    live_info = set()
    report_add = False
    report_counter = 0
    
    #state_fips_dict (dict): Dictionary of state FIPS.
    state_fips_dict = {
            "Alabama": '01', "Alaska": '02', "Arizona": '04', "Arkansas": '05',
            "California": '06', "Colorado": '08', "Connecticut": '09',
            "Delaware": 10, "District of Columbia": 11, "Florida": 12,
            "Georgia": 13, "Hawaii": 15, "Idaho": 16, "Illinois": 17,
            "Indiana": 18, "Iowa": 19, "Kansas": 20, "Kentucky": 21, 
            "Louisiana": 22, "Maine": 23, "Maryland": 24, "Massachusetts": 25,
            "Michigan": 26, "Minnesota": 27, "Mississippi": 28, "Missouri": 29,
            "Montana": 30, "Nebraska": 31, "Nevada": 32, "New Hamphsire": 33, 
            "New Jersey": 34, "New Mexico": 35, "New York": 36,
            "North Carolina": 37, "North Dakota": 38, "Ohio": 39, "Oklahoma": 40,
            "Oregon": 41, "Pennsylvania": 42, "Rhode Island": 44, 
            "South Carolina": 45, "South Dakota": 46, "Tennessee": 47,
            "Texas": 48, "Utah": 49, "Vermont": 50, "Virginia": 51, "Washington": 53,
            "West Virginia": 54, "Wisconsin": 55, "Wyoming": 56,
        }
    
    def add_report(self):
        """
        Prompts users to enter a new COVID report for any state for today's date
        with new COVID cases and new COVID deaths information.
        
        Attributes:
            today (str): Today's date.
            state (str): User's input state.
            valid_state (str): For validating if user input is a state.
            fips (str): state's FIPS code.
            cases (int): Number of COVID cases.
            deaths (int): Number of COVID deaths.
            start_over (str): Flag for adding or ending COVID report.
            info_obj (object): CovidInformation object
            
        Side Effects:
            Asks users for input.
            Changes date to current date.
            Writes to stdout.
            Modifies self.info.
            Modifies self.report_add.
            Modifies self.report_counter.
        
        Exception Handling:
            ValueError: handles invalid input.
        
        Returns:
            start_over (bool): Boolean expression to repeat process again.
        """
        today = date.today().strftime("%Y-%m-%d")
        print("Date: " + today)
        
        while True:
            try:
                state = input("Enter State(ex. Maryland): ")
                valid_state = ""
                for key in self.state_fips_dict:
                    if state == key:
                        valid_state = key             
            except ValueError:
                print("Please enter a state.")
                continue
            
            if valid_state == state:
                break
            
            else:
                print("Please enter a state.")
                continue
             
        fips = self.state_fips_dict.get(state)          
        print("State FIPS Code: " + str(fips))
        
        while True:
            try:
                cases = int(input("Enter cases reported: "))
            except ValueError:
                print("Please enter an integer.")
                continue
            if cases < 0:
                print("Please enter a positive integer.")
                continue
            else:
                break
        
        while True:
            try:
                deaths = int(input("Enter deaths reported: "))
            except ValueError:
                print("Please enter an integer.")
                continue
            if deaths < 0:
                print("Please enter a positive integer.")
                continue
            else:
                break
        
        while True:
            try:
                start_over = input("Would You Like To Add Another Report(Y/N): ")
                
            except ValueError:
                print("Please enter (Y/N).")
                
            if start_over == "Y" or start_over == "N":
                break
            else:
                print("Please enter (Y/N).")
                continue
        
        if CovidInfo(today, state, fips, cases, deaths) not in self.info:
            info_obj = CovidInfo(today, state, fips, cases, deaths)
            self.info.add(info_obj)
            self.report_counter = self.report_counter - 1
             
        self.report_add = True
            
        if start_over == 'N':
            start_over = False
            click.clear()
            
        elif start_over == 'Y':
            start_over = True
            click.clear()
        
        return start_over
    
    def read_file(self):
        """ 
        Extracts data from data.humdata.org API and stores information 
        into a set of objects. 
            
        Attributes:
            patient_data (DataFrame): Information for COVID reports
            date (str): COVID report date.
            state (str): COVID report state.
            fips (str): COVID report state FIP code.
            cases (int): COVID report for number of COVID cases.
            deaths (int): COVID report for number of COVID deaths.
            info_obj (object): CovidInformation object.
            
        Side Effects:
            Modifies self.info
            
        Returns:
            False: Boolean expression to break while loop
        """
        #Reads data from The New York Times API and stores it as a data frame.        
        patient_data = pd.read_csv(
            "https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-states.csv",
            usecols = ["date", "state", "fips", "cases", "deaths"]
            )
        
        live_patient_data = pd.read_csv(
            "https://raw.githubusercontent.com/nytimes/covid-19-data/master/live/us-states.csv",
            usecols = ["date", "state", "fips", "cases", "deaths"]
        )
            
        with click.progressbar(range(len(patient_data)), 
                                label = "Importing Data:") as bar:
                
            #Iterate through CSV and extract date, state, fips code, cases, and deaths.
            for i in bar:
                date = patient_data.values[i][0]
                state = patient_data.values[i][1]
                fips = patient_data.values[i][2]
                cases = patient_data.values[i][3]
                deaths = patient_data.values[i][4]
                    
                #Checks to see if there's no duplicates already in the set of objects.
                if CovidInfo(date, state, fips, cases, deaths) not in self.info:
                        
                    #Create object for COVID report and add it to the set.
                    info_obj = CovidInfo(date, state, fips, cases, deaths)
                    self.info.add(info_obj)
            
        #Iterate through LIVE CSV and extract date, state, fips code, cases, and deaths.
        for i in range(len(live_patient_data)):
            date = live_patient_data.values[i][0]
            state = live_patient_data.values[i][1]
            fips = live_patient_data.values[i][2]
            cases = live_patient_data.values[i][3]
            deaths = live_patient_data.values[i][4]
            
            if LiveCovidInfo(date, state, fips, cases, deaths) not in self.live_info:
                #Create object for COVID report and add it to the set.
                live_info_obj = LiveCovidInfo(date, state, fips, cases, deaths)
                self.live_info.add(live_info_obj)
                
        self.info.update(self.live_info)
        
        print("Importing Complete!")
        click.pause()
        click.clear()
        
    def write_file(self):
        """
        Writes from set of COVID report objects to a CSV file.
            
        Attributes:
            filename (str): Filename that is created in current directory.
            writer (writer object): Writer object to write to CSV file.
            
        Returns:
            False: boolean expression to break while loop.  
        """   
        with click.progressbar(self.info, label = "Downloading CSV File:", 
                                length = len(self.info)) as bar:
            filename = "Updated_Report.csv"
                
            #Creates new CSV file with columns named "Date, State, Fips, Cases, Deaths"
            with open(filename, 'w') as csv_file:
                writer = csv.writer(csv_file, delimiter = ',', lineterminator = '\n')
                writer.writerow(["Date", "State", "Fips", "Cases", "Deaths"])
                    
                #Writes to CSV in descending order by date and state
                for i in sorted(bar, key=lambda x: (x.get_date(), x.get_state())):
                    writer.writerow([i.get_date(), i.get_state(), i.get_fips(), 
                                    i.get_cases(), i.get_deaths()])
        
        with click.progressbar(self.live_info, label = "Downloading TXT File:",
                              length = len(self.live_info)) as bar:
            filename = "Latest Highest COVID Cases.txt"
            
            with open (filename, "w") as txt_file:
                writer = csv.writer(txt_file, delimiter = ',', lineterminator = '\n')
                writer.writerow(["Date As of: " + self.get_latest_report()])
                writer.writerow(["State", "Cases"])
                
                for i in sorted(bar, key=lambda x: (x.get_date(), x.get_state())):
                    writer.writerow([i.get_state(), i.get_cases()])
                     
        print("Download Complete!")
                
        click.pause()
        click.clear()
        
    def get_latest_report(self):
        """
        Gets the latest report date from the COVID set of objects.
        
        Attributes:
            sorted_report (list): Sorted COVID report objects from self.info.
            report_date (str): The latest report date.
            
        Side Effects:
            Modifies 
            
        Returns:
            report_date (str): The latest report date.
        """
        sorted_report = sorted(self.info, key=lambda x: (x.get_date(), x.get_state()))
        report_date = ""
        
        if self.report_add == False:
            report_date = sorted_report[-1].get_date()
        else:
            report_date = sorted_report[self.report_counter].get_date()
    
        return report_date
    
    def find_state(self):
        """ 
        This function will take an input from the user to search for a particular 
        state. The function will iterate through the most recent csv file or the 
        inputted report to find the most recent data for that state
            
        Attributes:
            valid_input_flag (int): Validates whether user input valid input
            state (str): The state the user wants to find latest information for.
            latest_report (str): The date of the latest COVID report.
            no_info (bool): Validates whether there's live data
            
            start_over (str): Whether or not the user wants to search for 
                              latest information for another state.
            
        Side Effects:
            Depends on self.info with having more than 1 COVID case.
         
        Returns: 
            start_over (bool): Boolean expression to repeat process again.
            False: If there's no data in application.
        """
        if (len(self.info) > 0):
            while True:
                try:
                    state = input("Enter State to Find Lastest Information For: ")
                    valid_state = ""
                    for key in self.state_fips_dict:
                        if state == key:
                            valid_state = key 
                            
                except ValueError:
                    click.clear()
                    print("Please enter a state.")
                
                if valid_state == state:
                    break
                else:
                    print("Please enter a state.")
                    continue
            
            latest_report = self.get_latest_report()
            no_info = True
            
            for i in sorted(self.info, key=lambda x: (x.get_date(), x.get_state()), 
                                                                                    reverse=True):
                if i.get_date() == latest_report:
                    if state == i.get_state():
                        fips = self.state_fips_dict.get(state)
                        print("Latest Information For: " + state + "\n")
                        print("Lastest Report As of: " + i.get_date())
                        print("State: " + i.get_state())        
                        print("State FIPS Code: " + str(fips))
                        print("Total Covid Cases: " + str(i.get_cases()))
                        print("Total Covid Deaths: " + str(i.get_deaths()))
                        no_info = False
                        
            if no_info == True:
                print("No Latest Information Provided.")
                    
            while True:
                try:
                    start_over = input("\nWould You Like To Search Another State(Y/N): ")
                    
                except ValueError:
                    print("Please enter (Y/N).")
                
                if start_over == "Y" or start_over == "N":
                    break
                else:
                    print("Please enter (Y/N).")
                    continue
            
            if start_over == 'N':
                start_over = False
                click.clear()
            
            elif start_over == 'Y':
                start_over = True
                click.clear()
                
            return start_over
        
        else:
            print("No data in the system.")
            click.pause()
            return False
    
    def latest_highest_deaths_rates(self):
        """
        Reads a csv file into a dataframe and groups it by states. 
        Then finds the total deaths the total cases for each state 
        for a specific date and sorts by highest to lowest number of deaths. 
            
        Returns:
            The states with the top ten highest deaths on this particular day
        
        Side Effect:
            Depends on whether or not CSV file has at least 10 reports.
        """
        date = input("Enter a date to search for highest death rates (YYYY-MM-DD): ")
        df = pd.read_csv("Updated_Report.csv", 
                         usecols=["Date", "State", "Cases", "Deaths"])
        df_2 = df.loc[df["Date"] == date]
        df_2["Death Rate"] = df_2["Deaths"]/df_2["Cases"]* 100
        df_2['Death Rate'].round(decimals=2)
        sorted_death_rate = df_2.sort_values(by=["Death Rate"], ascending=False)
        top_ten = sorted_death_rate[0:10]
        print(top_ten.to_string(index=False))
        death_rates_list = top_ten["Death Rate"].tolist()
        
        click.pause()
        click.clear()
        
        return death_rates_list
    
    def recent_most_case_area(self):
        """
        Reads data from the csv file that we download, calculate and print 
        the number of cases reported from date(input) to the recent date by states.
            
        Attributes:
            date (str): Covid report date.
            state (str): Covid report state.
            cases (int): Covid report  of number of COVID cases.
            
        Side effect:
            Relies on valid user input for date or else error will occur.
            Depends on CSV file to have at least 2 Covid cases for a state.
            prints zero value if there's only one case.
            prints to stdout.
            
        Return:
            result (list): The list of cases change value.
        """
        print("\nShow the Number of Cases reported from the date user put:\n")
        df = pd.read_csv("Updated_Report.csv", sep = ",")
        date_entry = input(' type the date in format YYYY-MM-DD : ')
        input_date = datetime.strftime(datetime.strptime(date_entry, 
                                                         '%Y-%m-%d'), '%Y-%m-%d')
        
        print(str(input_date) + "\t~\t" + str(date.today()-timedelta(days=1)) + "\n")
        range_cases = (df[df["Date"] >= input_date])
        
        max_cases = range_cases.groupby("State")["Cases"].max()
        min_cases = range_cases.groupby("State")["Cases"].min()
        
        change_cases = max_cases - min_cases
        print(change_cases.sort_values(ascending=False))
        result = change_cases.sort_values(ascending=False).tolist()
        
        
    
        click.pause()
        click.clear()
        return result 
        
    def recent_most_death_area(self):
        """
        Read data from the csv file that we download, calculate and print 
        the Number of death reported from date(input) to the recent date by states
        
        Attributes:
            date (str): Covid report date.
            state (str): Covid report state.
            deaths (int): Covid report of number of COVID deaths.
            
        Side effect:
            Relies on valid user input for date or else error will occur.
            Depends on CSV file to have at least 2 Covid cases for a state.
            prints zero value if there's only one case.
            Prints to stdout.
        """
        print("\nShow the Number of Deaths reported from the date user put:\n")
        df = pd.read_csv("Updated_Report.csv", sep = ",")
        date_entry = input(' type the date in format YYYY-MM-DD : ')
        input_date = datetime.strftime(datetime.strptime(date_entry,
                                                         '%Y-%m-%d'), '%Y-%m-%d')

        print(str(input_date) + "\t~\t" + str(date.today()-timedelta(days=1)) + "\n")
        range_death = (df[df["Date"] > input_date])
        
        max_deaths = range_death.groupby("State")["Deaths"].max()
        min_deaths = range_death.groupby("State")["Deaths"].min()
        
        change_deaths = max_deaths - min_deaths
        print(change_deaths.sort_values(ascending=False))
        
        click.pause()
        click.clear()
    
    def covid_cases_data(self):
        """ 
        This function will find name of the states and number of cases using
        live data, then append the data into two list called 
        states and cases.
        
        Attributes:
            state (list): The name of states.
            cases (list): The number of live cases.
            
        Returns:
            tuple - states and cases.
        """
        states = []
        cases = []
        
        for i in sorted(self.live_info, key=lambda x: (x.get_date(), x.get_state())):
            states.append(i.get_state())
            cases.append(i.get_cases())
            
        return (states, cases)
            
    def highest_cases_graph(self):
        """ 
        This function call covid_cases_data() function and retrieve data - list of states
        name and number of COVID cases. It convert two list into dictinary, then sort
        the values from highest to lowest. The sorted list of values is used to 
        get key from dictionary, then graph and display ten states with 
        highest number of cases.
        
        Attributes:
            x (tuple): tuples of states and cases.
            data (dict): convert tuples into dictionary.
            sort_data (list): sorts data by value
            x_value (list): adds all states into list.
            y_value (list): adds numbers of death to list.
        """
        x = self.covid_cases_data()
        data = dict(zip(x[0], x[1]))
        
        for key in data:
            data[key] =  int(data[key])
           
        sort_data = sorted(data, reverse=True, key=data.get)
        x_values = [x for x in sort_data]
        y_values = [data[y] for y in sort_data]
            
        plt.figure(figsize=(15,8))
        plt.bar(x_values[:10], y_values[:10])
            
        plt.title("Top 10 States With Highest Number of COVID-19 Cases            As of: " + self.get_latest_report())
        plt.xlabel("US States")
        plt.ylabel("COVID-19 Cases in Millions")
        plt.show()

def main():
    """
    Enter COVID reports, read COVID report information from humdata.org, 
    download COVID report file, find the latest number of cases/deaths 
    by state, list the top 10 states with highest death rates on a specific date, 
    prints total  cases/deaths reported from specific date to current date,
    show data visualization of COVID and exits application.
        
    Attributes:
        open_option (int): Flag for opening download report file 
                           option if user has Covid data.
                           
        option (str): Option user selected for application.
        
    Side Effects:
        Don't kill terminal. Instead exit from option menu in program.
    """

    while True:
        click.clear()
        print("US Covid Reporter")
        print("1. Enter Covid Report")
        print("2. Read Data from https://data.humdata.org")
        
        open_option = 3
        
        if len(CovidTrackerApp().info) > 0:
            print(str(open_option) + ". Download Updated Report")
            print(str(open_option + 1) + ". Find Latest Number of Cases/Deaths By State")
            open_option = 5
            
        if path.exists("Updated_Report.csv"):
            print(str(open_option) + 
                  ". List Top 10 States With Highest Death Rates On Specific Date")
            print(str(open_option + 1) + 
                  ". Print Total Cases Reported From Specific Date From Recent Case Report")
            print(str(open_option + 2) + 
                  ". Print Total Deaths Reported From Specific Date From Recent Death Report")
            print(str(open_option + 3) + 
                  ". Top 10 States With Covid-19 Cases Data Visualization")
            print(str(open_option + 4) + 
                  ". Exit Application")
    
        option = input("Option: ")

        if option == "1":
            while True:
                if CovidTrackerApp().add_report() == False:
                    break

        elif option == "2":
            CovidTrackerApp().read_file()
                
        elif option == "3": 
            CovidTrackerApp().write_file()
                
        elif option == "4":
            while True:
                if CovidTrackerApp().find_state() == False:
                    break
                    
        elif option == "5":
            CovidTrackerApp().latest_highest_deaths_rates()
                
        elif option == "6":
            CovidTrackerApp().recent_most_case_area()
                
        elif option == "7":
            CovidTrackerApp().recent_most_death_area()
                
        elif option =="8":
            CovidTrackerApp().highest_cases_graph()
            
        elif option == "9":
            os.remove("Updated_Report.csv")
            sys.exit()

        click.clear()
                 
if __name__ == "__main__":
    main()