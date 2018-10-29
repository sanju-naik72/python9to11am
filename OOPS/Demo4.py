class Employee:
    comp_name = "sathya"
    comp_cno = 9052492329
    @staticmethod
    def displayCompanyInfo():
        print(Employee.comp_name)
        print(Employee.comp_cno)

Employee.displayCompanyInfo()