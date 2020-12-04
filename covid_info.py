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
import sys

class Covid:
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
    """
   
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
    
    def parse_args(arglist):
        """This function will add two arguments - a path and a state and will pass the commandline arguments
        and will return the namespace
        
        """
        parser = ArgumentParser()
        parser.add_argument("path", type = str)
        parser.add_argument("state", type = str)
        return parser.parse_args(arglist)

    if__name__ == "__main__":
        args = parse_args(sys.argv[1:])
        value = positivity_rate(path=args.path, state=args.state)

    def testing_locations(filename, zip, location:
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

    def askUsers(self):
        """
        Diego
        This function will ask users if they have any symptoms relating to covid.
        All the data will be stored in a Person object that holds each indiviual person.
        
        parameters:
            self
            Person - A person object
        Attributes:
            name(str) - The name of the patient
            symptoms(list) - A list of symptoms
            covidTest(boolean) - A test to see if person has covid
            state(str) - State that they got infected in
        """
        
    def readFileAndStore(self, filename):
        """
        Diego
        This function will read in values from a file of patients.
        It will use regular expressions to sort information from file.
        Display the results and store them in individual Person objects in our dictionary.
        
        parameters:
            self
            filename - path to a file
        Attributes:
            patients(dict) - A dictionary to hold patient objects.
        """

    def reg_data(self, filename):
        """
        chandra
        This function will find state and numbers of deaths, number of tested postives,
        and number of tested negatives in the file and group it using regular expression,
        then it will be use for visualization.
        parameters:
            self
            filename(str) - path to file
        attributes:
            state(str) - state name
            death(int) - number of death in state
            positive(int) - number of tested positive
            negative(int) - number of tested negative
        """

    def graph(self):
        """
        chandra
        This function will visualize data using matplotlib. It will use values from reg_data() function.
        parameters:
            self
            Display graph when function is called.
        """

    def CaseDensity(self):
        """
        Minsung 
        This function will caculate covid density of each state and covid density of each state per day,month. 
        total population of each state/ total cases of each each = Covid density
        Covid density shows how dangerous each states actually are. 
        Parameters
            self
        Attributes
            positive_state (int) - number of tested positive(each state)
            population_state(int) - number of population (each state)
            positive(int) - number of tested positive
            covid_density(float) - population/positive cases. Lower covid density means more dangerous. 
        """

    def dailyMonthly(self):
        """
        Minsung
        This function will calculate the sum of cases each day, each month
        Calculate how many more/less people got infected than previous day/month
        Parameters
            self
        Attributes
            positive_state(int) - number of tested positive(each state)
            population_state(int) - number of population (each state)
            positive(int) - sum of number of tested positive
            Positive_month(int) - number of tested positve(month)
            positive_day(int) - number of tested positve(day)  
        """
