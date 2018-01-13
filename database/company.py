import json

class Company:
    def __init__(self):
        self.name = None
        self.url = None
        self.languages = None
        self.formality = None
        self.size = None
        self.locations = None

    def populate(self, json):
        self.name = json['name']
        self.url = json['url']
        self.languages = json['languages']
        self.formality = json['formality']
        self.size = json['size']
        self.locations = json['locations']

    def __str__(self):
        return self.name


companiesJSON = json.loads(open('database/companies.json').read())
companies = []

for company in companiesJSON:
    newComp = Company()
    newComp.populate(company)
    companies.append(newComp)


def suggestComp(formality, size, language):

    def dist(company):
        a1 = company.formality
        a2 = formality

        b1 = company.size
        b2 = size

        return ((int(a1) - int(a2))**2 + (int(b1) - int(b2))**2)**0.5

    temp = []
    for company in companies:
        if language in company.languages:
            temp.append(company)
    temp.sort(key=dist)
    return temp[:2]
