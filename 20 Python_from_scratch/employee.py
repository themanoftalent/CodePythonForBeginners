class Employee:

    raise_amaount=1.04
    number_of_employees=0
    
    def  __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.pay=pay
        self.emial=first+last+'@gmail.com'
        Employee.number_of_employees += 1
        
    def displayfirst(self):
        return '{} {}'.format(self.first,self.last)
    
    
    def emails(self):
        return self.first+self.last+'@gmail.com'
    
    #now we gotta give some pay rise
    def payRise(self):
        #self.pay=int(self.pay*1.04) when we dont want to make it manually we add a class variable
       # self.pay=int(self.pay*payRise) #firstError: first 'payRise' is not defined
        self.pay=int(self.pay*Employee.raise_amaount) #or we can say self.raise_amaount both works
    
#     @classmethod
#     def set_raise_amnt(cls, amount):
#         cls.raise_amaount=amount
        
#     @classmethod
#     def from_string(cls,emp_string):
#         first,last,pay=emp1_str.split('-')
#         return cls(first,last,pay)
        
#     @staticmethod
#     def is_workday(day):
#         if day.weekday()==5 or day.weekday()==6:
#             return False
#         return True
        
        
        
# emp1=Employee('Ahmet','Kaya',3400)
# emp2=Employee('Mahmut','Canik',1800)
# emp3=Employee('Can','Emlak',900)
# emp4=Employee('Cemil','Kaynak',5800)
# emp5=Employee('Hilal','Bengu',7600)
# #we can print like this but it takes too much time
# #print(emp1.first,emp1.last,emp1.emial,emp1.pay)


# Employee.set_raise_amnt(5) #= Employee.payRise(5)





# print(emp1.displayfirst())
# print(emp1.emails().lower())



# print('First payment',emp1.pay)
# emp1.raise_amaount=15.07
# emp1.payRise()
# print('After pay rise payment',emp1.pay)

# print('###################################')
# print(emp2.displayfirst())
# print(emp2.emails().lower())

# print('First payment',emp2.pay)
# emp2.payRise()
# print('After pay rise payment',emp2.pay)

# print('###################################')
# print(emp3.displayfirst())
# print(emp3.emails().lower())
# print('First payment',emp3.pay)
# emp3.raise_amaount=15.07
# emp3.payRise()
# print('After pay rise payment',emp3.pay)

# print('###################################')
# print(emp4.displayfirst())
# print(emp4.emails().lower())
# print('First payment',emp4.pay)
# emp4.raise_amaount=15.07
# emp4.payRise()
# print('After pay rise payment',emp4.pay)

# print('###################################')
# print(emp5.displayfirst())
# print(emp5.emails().lower())
# print('First payment',emp5.pay)
# emp5.raise_amaount=15.07
# emp5.payRise()
# print('After pay rise payment',emp5.pay)






# # print(emp1.__dict__)
# # print('###################################')
# # print(Employee.__dict__)
# print('The number of ',Employee.number_of_employees)

# emp1_str='Jake-Blunt-4500'
# emp2_str='Inna-Ayteyna-4000'


# first,last,pay=emp1_str.split('-')



# emp6=Employee(first,last,pay)

# print(emp6.first,end=' ')
# print(emp6.last)
# print(emp6.pay)
# print(emp6.emial.lower())





# emp6=Employee.from_string(emp1_str)
# print(emp6.first,end=' ')
# print(emp6.last)
# print(emp6.pay)
# print(emp6.emial.lower())
    
    

