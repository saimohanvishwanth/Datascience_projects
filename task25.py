class School:
    def __init__ (self,student_name,student_fathername,student_rollnumber,class_section):
        self.l= student_name
        self.k = student_fathername
        self.j= student_rollnumber
        self.h = class_section
    def output(self):
        print('student_name:', self.l)
        print('student_fathername:', self.k)
        print('student_rollnumber:', self.j)
        print('class_section:',self.h)
while True:
    p= input('enter the student_name:')
    o= input('enter the student_fathername:')
    i = input('enter the student_rollnumber:')
    u= input('enter the class_section:')

    Record= School(p,o,i,u)
    Record.output()