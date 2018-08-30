#! /usr/bin/env python
#coding=GB18030
class SchoolMember(object):
    '''ѧϰ��Ա����'''
    member = 0
 
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex
        self.enroll()
 
    def enroll(self):
        'ע��'
        print('just enrolled a new school member [%s].' % self.name)
        SchoolMember.member += 1
 
    def tell(self):
        print('----%s----' % self.name)
        for k, v in self.__dict__.items():
            print(k, v)
        print('----end-----')
 
    def __del__(self):
        print('������[%s]' % self.name)
        SchoolMember.member -= 1
 
 
class Teacher(SchoolMember):
    '��ʦ'
    def __init__(self, name, age, sex, salary, course):
        SchoolMember.__init__(self, name, age, sex)
        self.salary = salary
        self.course = course
 
    def teaching(self):
        print('Teacher [%s] is teaching [%s]' % (self.name, self.course))
 
 
class Student(SchoolMember):
    'ѧ��'
 
    def __init__(self, name, age, sex, course, tuition):
        SchoolMember.__init__(self, name, age, sex)
        self.course = course
        self.tuition = tuition
        self.amount = 0
 
    def pay_tuition(self, amount):
        print('student [%s] has just paied [%s]' % (self.name, amount))
        self.amount += amount
 
t1 = Teacher('Wusir', 28, 'M', 3000, 'python')
t1.tell()
s1 = Student('haitao', 38, 'M', 'python', 30000)
s1.tell()
s2 = Student('lichuang', 12, 'M', 'python', 11000)
print(SchoolMember.member)
del s2
 
print(SchoolMember.member)