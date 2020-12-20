# Programmers Kristen Wagner, Chandra Tamang, Minsung Kim, and Diego Amores
import click
import csv
import pandas as pd
import os.path
from os import path
import sys
import matplotlib.pyplot as plt
import re
from CovidInformation import CovidInfo
from datetime import date, datetime, timedelta

"""
INST 326 Object Oriented Programming Final Project
Group - 107
Prof: Aric Bills
"""

class CovidTrackerApp():
    """
    CovidTrackerApp class has 10 different functions, and all functions have
    different purposes.
    
    get_report()
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
    
    reg_data()
        This function will use regular expression to access states and death 
        values and return a tuple of state and deaths.
    
    graph()
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
    
    def get_report(self):
        """
        Prompts users to enter a new COVID report for any state for today's date
        with new COVID cases and new COVID deaths information.
        
        Attributes:
            valid_input_flag (int): Flag for input valdidation.
            today (str): Today's date.
            state (str): User's input state.
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
            start_over (bool): 
            
        Few Exception Bugs to fix.
        """
        valid_input_flag = 0
        while True:
            
            today = date.today().strftime("%Y-%m-%d")
            print("Date: " + today)

            while True:
                try:
                    state = input("Enter State(ex. Maryland): ")
                    
                    for key in self.state_fips_dict:
                        if key == state:
                            valid_input_flag = 1
                        
                    if valid_input_flag == 1:
                        break
                    else:
                        raise ValueError() 
                      
                except ValueError:
                    click.clear()
                    print("Invalid input! Please try again...")
                            
            fips = self.state_fips_dict.get(state)          
            print("State FIPS Code: " + str(fips))
            
            while True:
                try:
                    cases = int(input("Enter cases reported: "))
                    if cases < 0:
                        raise ValueError()
                    
                    while True:
                        try:
                            deaths = int(input("Enter deaths reported: "))
                            if deaths < 0:
                                raise ValueError()
                            break
                        
                        except ValueError:
                            click.clear()
                            print("Input only positive integers! Please try again...")
                    break
                
                except ValueError:
                    click.clear()
                    print("Input only positive integers! Please try again...")
                      
            while True:
                try:
                    start_over = input("Would You Like To Add Another Report(Y/N): ")
                    if start_over == 'N':
                        break
                    elif start_over == 'Y':
                        click.clear()
                        break
                    else:
                        raise ValueError()
                    
                except ValueError:
                    click.clear()
                    print("Input Invalid. Please try again...")
            
            if CovidInfo(today, state, fips, cases, deaths) not in self.info:
                info_obj = CovidInfo(today, state, fips, cases, deaths)
                self.info.add(info_obj)
                
                self.report_counter = self.report_counter - 1
                
            self.report_add = True
            
            if start_over == 'N':
                start_over = False
                click.clear()
                break
            else:
                valid_input_flag = 0
                continue

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
        while True:
            
            #Reads data from CSV and stores it has a data frame.        
            patient_data = pd.read_csv(
                "https://data.humdata.org/hxlproxy/api/data-preview.csv?url=https%3A%2F%2Fraw.githubusercontent.com%2Fnytimes%2Fcovid-19-data%2Fmaster%2Fus-states.csv&filename=us-states.csv",
                usecols = ["date", "state", "fips", "cases", "deaths"])
            
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
                        
                print("Importing Complete!")
                click.pause()
                click.clear()
            
            return False
        
    def write_file(self):
        """
        Writes from set of COVID report objects to a CSV file.
            
        Attributes:
            filename (str): Filename that is created in current directory.
            writer (writer object): Writer object to write to CSV file.
            
        Returns:
            False: boolean expression to break while loop.  
        """
        while True:   
            with click.progressbar(self.info, label = "Downloading File:", 
                                   length = len(self.info)) as bar:
                filename = "Updated_Report.csv"
                
                #Creates new CSV file with columns named "Date, State, Fips, Cases, Deaths"
                with open(filename, 'w') as csv_file:
                    writer = csv.writer(csv_file, delimiter = ',', lineterminator = '\n')
                    writer.writerow(["Date", "State", "Fips", "Cases", "Deaths"])
                    
                    #Writes to CSV in descending order by date and state
                    for i in sorted(bar, key=lambda x: (x.get_date(), x.get_state()), reverse=True):
                        writer.writerow([i.get_date(), i.get_state(), i.get_fips(), 
                                        i.get_cases(), i.get_deaths()])
                        
                print("Download Complete!")
                click.pause()
                click.clear()
                
            return False