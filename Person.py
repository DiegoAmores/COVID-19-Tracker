class Person:
    _name = ''
    _covid_test = ''
    _gender = ''
    _birth_date = ''
    _location = ''
    _symptom = ''
        
    def setName(self, attr):
        Person._name = attr
        
    def getName(self):
        return Person._name
    
    def setCovidTest(self, attr):
        Person._covid_test = attr
    
    def getCovidTest(self):
        return Person._covid_test
    
    def setGender(self, attr):
        Person._gender = attr
    
    def getGender(self):
        return Person._gender
    
    def setBirthDate(self, attr):
        Person._birth_date = attr
    
    def getBirthDate(self):
        return Person._birth_date
    
    def setLocation(self, attr):
        Person._location = attr
    
    def getLocation(self):
        return Person._location
    
    def setSymptom(self, attr):
        Person._symptom = attr
    
    def getSymptom(self):
        return Person._symptom