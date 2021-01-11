#Programmer: Diego Amores
# COVID Report Object Class

class CovidInfo:
    date = ""
    state = ""
    fips = 0
    cases = 0
    deaths = 0
    
    def __init__(self, date, state, fips, cases, deaths):
        self.date = date
        self.state = state
        self.fips = fips
        self.cases = cases
        self.deaths = deaths
        
    #compares COVID reports.
    def __eq__(self, other):
        return (self.date, self.state) == (other.date, other.state)
    
    #creates hashcode for COVID object based on date and state.
    def __hash__(self):
        return hash((self.date, self.state))
    
    #gets the date of a COVID report.
    def get_date(self):
        return self.date
    
    #gets the state of a COVID report.
    def get_state(self):
        return self.state
    
    #gets the fips code of a state.
    def get_fips(self):
        return self.fips
    
    #gets the number of cases of a COVID report.
    def get_cases(self):
        return self.cases
    
    #gets the number of deaths of a COVID report.
    def get_deaths(self):
        return self.deaths