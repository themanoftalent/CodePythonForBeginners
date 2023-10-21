##################################################
#### **************************************** ####
#### !/usr/bin/python3                        ####
#### -*- coding: utf-8 -*-                    ####
#### @Time    : 2023/20/10 11:40              ####
#### @Author  : themanoftalent                ####
#### @Site:https://github.com/themanoftalent  ####
#### @Project : python-app                    ####
#### **************************************** ####
##################################################
# init is initilaizing
'''self as it suggests, refers to itself- the object which has called the method.
That is, if you have N objects calling the method, then self.a will refer to a separate
instance of the variable for each of the N objects. Imagine N copies of the variable a for each object
__init__ is what is called as a constructor in other OOP languages such as C++/Java. The basic idea is
 that it is a special method which is automatically called when an object of that Class is created
'''

class Person:
    '''Doc - Inside Class '''

    def __init__(self, name):
        '''Doc - __init__ Constructor'''
        self.name = name
        self.email=name+'@mail.com'

    def show(self, n1, n2):
        '''Add two numbers'''
        return 'Toplam = ', (n1 + n2)


    def __repr__(self):
        '''Add two numbers'''
        return 'The names in the class is : {} {}'.format(self.name,self.email) 

    def __str__(self):
        '''Add two numbers'''
        return 'How to stop a problem without try ' 




class Developer(Person):
           """inherit the upper class"""

           def __init__(self,name, pay,pro_lang):
            super().__init__(name)
            self.pay = pay
            self.pro_lang = pro_lang


           def displayLang(self):
            return self.pro_lang         
        

    # def __del__(self):
    #     print('Destructor Deleting object - ', self.n_name)


p1 = Person('Janset')

d1=Developer('Hasan','Python',5400)

print (p1.name)
print(p1.show(2, 3))
print(p1.email)
print(p1) #lets use __repr__ to get rid of mistake

print('\nThe developer is ',d1.name,end=' ')
print('he knows python and his salary is',d1.displayLang(),end=', his email address is ')
print(d1.email)


# print(d1.__str__())
# print(d1.__repr__())
# print('\n')
# print(p1.__doc__)
# print(p1.__init__.__doc__)
# print(p1.show.__doc__)
