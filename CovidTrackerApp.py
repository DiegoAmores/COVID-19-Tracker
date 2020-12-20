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