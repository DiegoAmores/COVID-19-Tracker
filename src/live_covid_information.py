#Programmer: Diego Amores

class LiveCovidInfo:
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
        
    def __eq__(self, other):
        return (self.date, self.state) == (other.date, other.state)
    
    def __hash__(self):
        return hash((self.date, self.state))
    
    def get_date(self):
        return self.date
    
    def get_state(self):
        return self.state
    
    def get_fips(self):
        return self.fips
    
    def get_cases(self):
        return self.cases
    
    def get_deaths(self):
        return self.deaths