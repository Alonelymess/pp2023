
from domains.StudentManager import StudentManager  
from domains.Utils import Utils
from domains.CoursesManager import CoursesManager
import numpy as np
class Manager(Utils):
    def __init__(self):
        self.__student_manager = StudentManager()
        self.__course_manager = CoursesManager()

    def add_Info(self):
        while True:
            print('\nEnter your choice:')
            print('1. Add student')
            print('2. Add course')
            print('3. Add student to course')
            print('4. Cancel')
            choice = input('Choice: ')
            if choice == '1':
                self.__student_manager.add_Students()
            elif choice == '2':
                self.__course_manager.add_Course()
            elif choice == '3':
                student_list = self.__student_manager.get_Student_list()
                course_list = self.__course_manager.get_Course_list()

                if len(course_list) == 0:
                    print('No course currently active!')
                    return

                while True:
                    try:
                        course_id = int(input('Enter course ID that you want to add students : '))
                        break
                    except ValueError:
                        print('Invalid input!')

                while self.check_Id(course_id) == False:
                    course_id = int(input('Please enter valid course ID: '))
                for i in course_list:
                    if i.get_Id() == course_id:
                        i.set_Students_learnt(student_list, course_id)
            elif choice == '4':
                return
            else:
                print('Invalid input!')

    def change_Info(self):
        while True:
            print('\nEnter your choice:')
            print('1. Change student')
            print('2. Change course')
            print('3. Cancel')
            choice = input('Choice: ')
            if choice == '1':
                self.__student_manager.change_Student()
            elif choice == '2':
                self.__course_manager.change_Course()
            elif choice == '3':
                return
            else:
                print('Invalid input!')

    def remove_Info(self):
        while True:
            print('\nEnter your choice:')
            print('1. Remove student')
            print('2. Remove course')
            print('3. Cancel')
            choice = input('Choice: ')
            if choice == '1':
                self.__student_manager.remove_Students()
            elif choice == '2':
                self.__course_manager.remove_Course()
            elif choice == '3':
                return
            else:
                print('Invalid input!')



    def search_Student(self):

        student_id = int(input('Enter student ID: '))
        while self.check_Id(student_id) == False:
            student_id = int(input('Please enter valid student ID: '))

        for i in self.__student_manager.get_Student_list():
            if i.get_Id() == student_id:
                i.show_Student()

                gpa = np.zeros(1)
                for k in self.__course_manager.get_Course_list():
                    for j in k.get_Students_learnt():
                        if student_id == j[0].get_Id():
                            print(f'    Course learnt: {k.get_Name()}    ID: {k.get_Id()}  Mark: {j[1]}')
                            gpa = np.append(gpa, j[1]/k.get_Credits())
                
                print('    GPA: ', np.sum(gpa))

                return
             
            
        print('Student not found')


    def search_Course(self):

        course_id = int(input('Enter course ID: '))
        while self.check_Id(course_id) == False:
            course_id = int(input('Please enter valid course ID: '))

        for i in self.__course_manager.get_Course_list():
            if i.get_Id() == course_id:
                i.show_Course()

                for k in i.get_Students_learnt():
                    print(f'    Student in this course: {k.show_Student()}    Mark: {k[1]}')

                return
             
            
        print('Course not found')


    def get_Info(self):
        while True:
            print('\nEnter your choice: ')
            print('1. Search student ')
            print('2. Search course ')
            print('3. Show all students ')
            print('4. Show all courses ')
            print('5. Cancel')
            choice = input('Choice: ')
            if choice == '1':
                self.search_Student()
            elif choice == '2':
                self.search_Course()
            elif choice == '3':
                self.__student_manager.show_Students()
            elif choice == '4':
                self.__course_manager.show_Courses()
            elif choice == '5':
                return
            else:
                print('Please enter valid choice!')
