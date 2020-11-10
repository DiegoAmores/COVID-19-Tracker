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
    class will have 8 different functions please list your functions below.
    """
    # please add your function here
    
    def positivity_rate(self, filename):
        """
        Kristen 
        This function will prompt the user to input a state, and will output the positivity rate for that 
        specific area and a letter grade for that state. The data will be stored in a separate file and be read when prompted by the user
        parameters: 
            self
            filename - path do a file
        Attributes:
            state(str) - The state that is being considered
            positivity rate(int) - Percentage of the population that is positive
            letter grade (str) - The letter grade (A-D) given based on the number of positive cases in the state

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
        This function will find state and numbers of deaths, postive,
        and negative in the file and group it using regular expression, then it will be use for visualization.
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
        """
    def dailyMontly(self):
        """
        Minsung
        This function will calculate the sum of cases each day, each month
        Calculate how many more/less people got infected than previous day/month
        """
