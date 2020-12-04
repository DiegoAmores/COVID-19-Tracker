from Person import Person
from argparse import ArgumentParser
import re
import sys

"""
INST 326 FINAL PROJECT
Group - 107
Prof: Aric Bills

Chandra Tamang
Kristen Wagner
Minsung Kim
Diego Amores
"""
import pandas as pd 

class CovidTracker(Person):
    """
    Covid class have 8 different functions, and all of the functions have different purposes.
    positivity_rate()
        This function will prompt users and base on users input, it will print out positivity rate,
        letter grade for state, and so on. It also store users input, and it can be later read by users.
    send_message()
        This function will send users friends message if users experienced symptoms of covid,
        or tested positive for covid.
    askUsers(self)
        This function promt users and their inputs will be stored in a Person object
        that holds each indiviual person.
    readFileAndStore()
        This function will read patients file.
        Display the results and store them in individual Person objects in our dictionary.
    reg_data()
        This function will use regular expression to group data about covid such as state, number of deaths,
        and number of tested positives, and number of tested negatives.
    graph()
        This function will use values from reg_data function to visualize data,
        and then it will display the results.
    CaseDensity()
        This function will caculate covid density of each state and covid density of each state per day,
        and month. The total population of each state/ total cases of each each = Covid density
        Covid density shows how dangerous each states actually are. 
    dailyMonthly()
        This function will calculate the sum of cases each day, and each month
        Calculate how many more/less people got infected than previous day/month
    attributes:
    self
        filename - path to filename
    """
    def __init__(self):
        self.patients = []
   
    def positivity_rate(path, state):
        """
        Kristen 
        Data found from: https://github.com/CSSEGISandData/COVID-19/blob/master/csse_covid_19_data/csse_covid_19_daily_reports_us/12-02-2020.csv
        This function will prompt the user for a state and will read a csv file, then output 
        the total number of covid cases in that state thus far, the current active cases, and the 
        incident rate, which is the number of new cases per day divided by a population of 1,000 people. 
        
        Parameters: 
            path(str)- path to a file
            state(str) - The state that is being considered
            total_cases (int) - Number of cases reported so far for this state
            active_cases (int) - Number of active reported covid cases
            incident rate (int) - Number of cases per day per 1,000 people
            
        """    
        df = pd.read_csv("covid_data.csv")
        cols = ["Province_State", "total_cases", "Active", "Incident_rate"]
        df2 = df[cols]
        incidence = max(df2["Incident_rate"])
        top_five = incidence.head(n=5)
        print(top_five)

    def testing_locations(filename, zip, location):
        """
        Kristen
        This function will prompt a user to input their zip code(in Maryland), and will output 
        testing locations that are closest to them and the address of the testing site.
        parameters:
        
        Parameters: 
            filename (str)- The file that will have the zip codes and 
            zip (string) - the zip code of the user 
            testing_location (str) - Nearest testing site to the user 
            
        """
        
    def patientInfo(self, name, covid_test, gender, birthdate, location, symptoms, lisPatients):
        """
        Diego
        This function will prompt patients for information such as full name, covid results, gender,
        birthdate, location, and symptoms. It will also prompt the users to enter data for other patients 
        and whether or not to display a list of patients.
        
        Parameters:
            name (str) - The full name of a patient
            covid_result - Result of covid test
            gender - The gender of patient
            birthdate - The birthdate of a patient
            location - The last know location before coming into contact with COVID
            symptoms - Symptoms that patients experienced
        """
        info = CovidTracker()
        info.setName(name)
        info.setCovidTest(covid_test)
        info.setGender(gender)
        info.setBirthDate(birthdate)
        info.setLocation(location)
        info.setSymptom(symptoms)
        
        self.patients.append(info)
        
        #Will be printing out a list of patients if user wants to
        if lisPatients == 'Yes' or lisPatients == 'yes' or lisPatients == 'Y':
            for patients in self.patients:
                print(patients.getName())
        #will implement a algorthimn for searching patients
        
    def readFileAndStore(self, filename):
        """
        Diego
        This function will read in values from a  csv file of patients.
        It will use regular expressions to sort information from file.
        We will also be inserting new patient information into the csv file.
        We will be displaying the results and store them into another csv file.
        
        parameters:
            self
            filename - path to a file
        Attributes:
            patients(dict) - A dictionary to hold patient objects.
        """

    def CaseDensity(filename, state):
        """
        Minsung 
        This function will caculate covid density of each state and covid density of each state per day,month. 
        Parameters
            self
        Attributes
            positive(int) - number of tested positive
            covid_density(float) - population/positive cases. Lower covid density means more dangerous. 
            Total_cases (int) - number of tested positive
            population(int) - number of population (each state)
            covidDensity(float) - population/positive cases. Lower covid density means more dangerous. 
        """
        df = pd.read_csv("covid_data.csv", sep = ",")
        df["caseDensity"] = df["population"]/df["Total_case"]*100
        return print(df[["state", "Total_cases", "caseDensity"]].sort_values(by=['Total_cases'], ascending=False).head())


    def highest_density(filename,state):
        """
        Minsung
        This function will show the highest case density state
        Parameters
            state
            filename
        Attributes
            state(str) - name of state
            positive(int) - sum of number of tested positive
            Positive_month(int) - number of tested positve(month)
            positive_day(int) - number of tested positve(day)  
            covidDensity(float) - population/positive cases. Lower covid density means more dangerous. 
            State
        """
        df = pd.read_csv("covid_data.csv", sep = ",")
        filt = df[df["state"] == state]
        maxx = filt["case_density"].max()
        state_filt = filt[filt["caseDensity"] == maxx]["state"].iloc[0]
        return maxx, state_filt 

def reg_data(filename):

    """
    chandra
    This function will find state and numbers of deaths, number of tested postives,
    and number of tested negatives in the file using regular expression, and added to the list
    it will be use for visualization.
    parameters:
        self
        filename(str) - path to file
    attributes:
        state(str) - state name
        death(int) - number of death in state
        positive(int) - number of tested positive
        negative(int) - number of tested negative
    """
    with open(filename, "r", encoding='utf-8') as f:
        new_list = []
        for line in f:
            # state = r"(\w.+\.)(\s\d+\,?\d+)(\s\d+\,?\d+\,?\d+)"
            state = re.search(r"(\w.+\.)", line)
            num_death = re.search(r"(\s\d+\,?\d+)", line)
            num_positive = re.search(r"(\s\s\d+\,?\d+)", line)

            if state:
                states = state[1]
                new_list.append(states)
            if num_death:
                death = num_death[1]
                new_list.append(death)
            if num_positive:
                positive = num_positive[1]
                new_list.append(positive)
    print(new_list)

def graph(self):
    """
    chandra
    This function will visualize data using matplotlib. It will use values from reg_data() function.
    parameters:
    self
    Display graph when function is called.
    """

def parse_args(arglist):
    """ Parse command-line arguments. """
    parser = ArgumentParser()
    parser.add_argument("filename",
                    help="file containing states, deaths, positives")
    parser.add_argument("path", type = str)
    parser.add_argument("state", type = str)
    return parser.parse_args(arglist)

def main():
    
    while True:
        
        name = input("Enter Full Name: ")
        print("Lab Test: COVID-19")
        covid_test = input("Result: ")
        gender = input("Enter Gender: ")
        birthdate = input("Enter Birth Date: ")
        location = input("Enter Last Known Location of Infection: ")
        symptoms = input("Enter Symptoms After Infection: ")
        lisPatients = input("List all patients: ")
        startOver = input("Would You Like To Include Another Patient: ")
        
        c = CovidTracker()
        c.patientInfo(name, covid_test, gender, birthdate, location, symptoms, lisPatients)
        
        if startOver == 'no' or startOver == 'No' or startOver == 'N':
            break
        else:
            continue
            
if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    reg_data(args.filename)
    main()
    positivity_rate(path=args.path, state=args.state)
    
