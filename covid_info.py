"""
INST 326 FINAL PROJECT
Group - 107
Prof: Aric Bills

Chandra Tamang
Kristen Wagner
Minsung Kim
Diego Amores
"""
class covid:
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
    # please add your functions here
    def positivity_rate(self, filename):
        """
        Kristen 
        This function will prompt the user to input a state, and will output the positivity rate for that 
        specific area and a letter grade for that state. The data will be stored in a separate file,
        and be read when prompted by the user
        parameters: 
            self
            filename - path do a file
        Attributes:
            state(str) - The state that is being considered
            positivity rate(int) - Percentage of the population that is positive
            letter grade (str) - The letter grade (A-D) given based on the number of positive cases
            in the state

        """ 

    def send_message(self):
        """
        Kristen
        This method will send a message to the user if he/she has come into contact with and 
        individual who has tested positive for COVID-19.
        parameters:
            self
        """

    def askUsers(self):
        """
        Diego
        This function will ask users if they have any symptoms relating to covid.
        All the data will be stored in a Person object that holds each indiviual person.
        """
        
    def readFileAndStore(self, filename):
        """
        Diego
        This function will read in values from a file of patients.
        Display the results and store them in individual Person objects in our dictionary.
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
