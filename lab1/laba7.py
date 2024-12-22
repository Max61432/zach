class Employer:
    
    def __init__ (self, name, id):
        self.name = name
        self.id = id 
    
    def get_info (self):
        print (self.name, self.id)


class Manager (Employer):

    def __init__ (self, name, id, department):
        self.department = department
        super().__init__ (name, id)
        

    def manage_project (self):
        print ('ok')


class Technician (Employer):

    def __init__ (self, name, id, specialization):
        self.specialization = specialization
        super().__init__ (name, id)

    def perform_maintenance (self):
        print ('done')


class TechManager (Technician, Manager):

    def __init__ (self,name, id, specialization, departament):
        super().__init__(name, id, specialization)
        super().__init__(name, id, departament)
    
    def get_info(self):
        print(self.name, self.id, self.department, self.specialization)

a = TechManager ('aa','11',1,5)
a.get_info()