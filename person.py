from tax import Income

class Residents():
    def __init__(self,spose=False,income=0):
        self.income = income

    def spouse(self):
        pass

    def get_incometax(self,employmentincome,realpropertyincome,sposeincome,**kwargs):
        return Income(employmentincome=employmentincome,
                      realpropertyincome=realpropertyincome,
                      sposeincome=sposeincome
                      ).get_tax(**kwargs)
