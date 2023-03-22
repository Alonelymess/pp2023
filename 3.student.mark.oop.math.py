import math
import numpy as np

'''
    Utils class:
        attribute: name, id
        method: set_Name, set_Id, get_Name, get_Id, check_Id
    
    Student class(Utils):
        attribute: name, id, dob
        method: set_Name, set_Id, set_Dob, get_Name, get_Id, get_Dob, check_Id

    Student Manager class(Student):
        attribute: students
        method: add_Students change_Student, remove_Students, show_Students, get_Student_list

    Course class:
        attribute: name, ID
        method: set_Name, set_Id, get_Name, get_Id, check_Id

    Courses Manager class:
        attribute: courses
        method: add_Courses, change_Course, remove_Courses, show_Courses, get_Courses_list

    Manager class:
        attribute: student_manager, courses_manager
        method: add_Info, remove_Info, change_Info, search_Student, search_Course           
'''


class Utils:
    def __init__(self, args):
        self.set_Name(args)
        self.set_Id(args)
         
    def set_Name(self, args):
        self._name = input(f'Enter {args} name: ')
        while len(self._name) == 0 or not self._name.isalpha():
            self._name = input(f'Please enter valid {args} name: ')

    def set_Id(self, args):
        self._id = int(input(f'Enter {args} ID: '))
        while self.check_Id(self._id) == False:
            self._id = int(input(f'Please enter valid {args} ID: '))

    def get_Name(self):
        return self._name

    def get_Id(self):
        return self._id
    
    def check_Id(self, id):
        if id < 0:
            print('Invalid ID')
            return False
        return True


class Student(Utils):
    def __init__(self):
        super().__init__('student')
        self.set_Dob()

    def set_Dob(self):
        self.__dob = input('Enter student date of birth: ')

    def get_Dob(self):
        return self.__dob

    def show_Student(self):
        print(f'    Name: {self.get_Name()}    ID: {self.get_Id()}    Dob: {self.get_Dob()}')



class StudentManager(Student):
    def __init__(self):
        self.__students = []

    def search(self, id):
        for i in self.__students:
            if i.get_Id() == id:
                return i
        return False

    def add_Students(self):
        while True:
            try:
                count = int(input('Enter number of new students: '))
                break
            except ValueError:
                 print('Invalid number of students!')
            

        for i in range(count):
            new_student = Student()
            if len(self.__students) == 0: # if there is no student in the list
                self.__students.append(new_student)
                continue

            found = self.search(new_student.get_Id())
            while found != False:
                print('Student already exists! ')
                print('Please enter new student information!')

                new_student = Student()
                found = self.search(new_student.get_Id())
            self.__students.append(new_student)

    def change_Student(self):
        student_id = int(input('Enter student ID: '))
        while self.check_Id(student_id) == False:
            student_id = int(input('Please enter valid student ID: '))

        found = self.search(student_id)
        if found == False:
            print('Student not found!')
            return

        print('Student found!\n')
        while True:
            print('Enter choice:')
            print('1. Change name')
            print('2. Change ID')
            print('3. Change date of birth')
            print('4. Cancel')
            choice = input('Enter choice: ')
            if choice == '1':
                found.set_Name()
                print('Change name success!')
            elif choice == '2':
                found.set_Id()
                print('Change ID success!')
            elif choice == '3':
                found.set_Dob()
                print('Change date of birth success!')
            elif choice == '4':
                print('Change cancel!')
                return
            else:
                print('Invalid choice!')


    def remove_Students(self):
        if len(self.__students) == 0: # if there is no student in the list
            print('No student found!')
            return

        while True:
            try:
                count = int(input('Enter number of deleted students: '))
                if count > len(self.__students) or count <= 0:
                    print('Invalid number of students to be removed!')
                    print('Currently there are', len(self.__students), 'students in the list!')
                    continue
                break
            except ValueError:
                 print('Invalid number of students!')

        
            return
        for i in range(count):
            student_id = int(input('Enter student ID: '))

            while self.check_Id(student_id) == False:
                student_id = int(input('Please enter valid student ID: '))

            for i in self.__students:
                found = self.search(student_id)
                if found != False:
                    self.__students.remove(i)
                    print('Student removed!')
                else:
                    print('Student not found')

    def get_Student_list(self):
        return self.__students

   
    def show_Students(self):
        if len(self.__students) == 0:
            print('No student found!')
            return
        for i in self.__students:
            i.show_Student()


class Course(Utils):
    def __init__(self):
        super().__init__('course')
        self.set_Credits()
        self.__students_learnt = []

    def set_Credits(self):
        while True:
            try:
                self.__credits = int(input('Enter number of credits: '))
                break
            except ValueError:
                print('Invalid number of credits!')

    def get_Credits(self):
        return self.__credits

    def search(self, id):
        for i in self.__students_learnt:
            if i[0].get_Id() == id:
                return i
        return False

    def set_Students_learnt(self, students_list, courses_id):
        

        while True:
            try:
                count = int(input(f'Enter number of students learnt course ID {courses_id}: '))
                break
            except ValueError:
                 print('Invalid number of students!')

        for i in range(count):
            student_id = int(input(f'Enter student {i+1} ID learn this course: '))
            
            while self.check_Id(student_id) == False:
                student_id = input(f'Please enter valid student {i+1} ID learn this course: ')

            
            if self.search(student_id) != False: 
                print('Student already learnt this course!')
                return

            found = False
            for j in students_list:
                if student_id == j.get_Id():
                    found = j

            while found == False:
                print('Student not found!')
                student_id = int(input(f'Enter right student {i} ID learn this course: '))

            mark = math.floor(float(input('Enter mark of this student: ')))
            while mark < 0 or mark > 20:
                mark = int(input('Please enter valid mark of this student: '))
            self.__students_learnt.append((found, mark))
            

    def get_Students_learnt(self):
        return self.__students_learnt

    def show_Course(self):
        print(f'    Name: {self.get_Name()}    ID: {self.get_Id()}')


class CoursesManager(Course):
    def __init__(self):
        self.__courses = []

    def search(self, id):
        for i in self.__courses:
            if i.get_Id() == id:
                return i
        return False

    def add_Course(self):
        while True:
            try:
                count = int(input('Enter number of new courses: '))
                break
            except ValueError:
                 print('Invalid number of courses!')

        for i in range(count):
            new_course = Course()
            found = self.search(new_course.get_Id())
            while found != False:
                print('Course already exists! ')
                print('Please enter new course information!')
                new_course = Course()
                found = self.search(new_course.get_Id())
            self.__courses.append(new_course)

    def change_Course(self):
        course_id = int(input('Enter course ID: '))
        while self.check_Id(course_id) == False:
            course_id = int(input('Please enter valid course ID: '))

        found = self.search(course_id)
        if found == False:
            print('Course not found!')
            return

        print('Course found!\n')
        while True:
            print('Enter choice:')
            print('1. Change name')
            print('2. Change ID')
            print('3. Change mark')
            print('4. Cancel')
            choice = input('Enter choice: ')
            if choice == '1':
                found.set_Name()
                print('Change name success!')
            elif choice == '2':
                found.set_Id()
                print('Change ID success!')
            elif choice == '3':
                change_student_id = int(input('Enter student ID need to change: '))
                for i in found.get_Students_learnt():
                    if i[0].get_Id() == change_student_id:
                        mark = int(input('Enter new mark: '))
                        while mark < 0 or mark > 20:
                            mark = int(input('Please enter valid mark: '))
                        i[1] = mark
                        print('Change mark success!')
                        return
            elif choice == '4':
                print('Change cancel!')
                break
            else:
                print('Invalid choice!')

    def remove_Course(self):
        if len(self.__courses) == 0: # if there is no course in the list
            print('No course found!')
            return

        while True:
            try:
                count = int(input('Enter number of deleted courses: '))
                if count > len(self.__courses) or count <= 0:
                    print('Invalid number of courses to be removed!')
                    print('Currently there are', len(self.__courses), 'courses in the list!')
                    continue
                break
            except ValueError:
                 print('Invalid number of courses!')

        
        for i in range(count):
            course_id = int(input('Enter course ID: '))

            while self.check_Id(course_id) == False:
                course_id = int(input('Please enter valid course ID: '))

            for i in self.__courses:
                if i.get_Id() == course_id:
                    self.__courses.remove(i)
                    print('Course removed!')
                    return
            print('Course not found')

    def show_Courses(self):
        if len(self.__courses) == 0:
            print('No course found!')
            return

        print('Courses:')
        for i in self.__courses:
            i.show_Course()

    def get_Course_list(self):
        return self.__courses

            
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

                found = False
                for i in course_list:
                    if i.get_Id() == course_id:
                        found = True
                        i.set_Students_learnt(student_list, course_id)

                if found == False:
                    print('Course not found!')

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

                gpa = np.empty(1)
                for k in self.__course_manager.get_Course_list():
                    for j in k.get_Students_learnt():
                        if student_id == j[0].get_Id():
                            print(f'    Course learnt: {k.get_Name()}    ID: {k.get_Id()}  Mark: {j[1]}')
                            gpa = np.append(gpa, j[1]/k.get_Credits())
                
                print('    GPA: ', np.sum(gpa).round(2))

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
            
def main():
    manager = Manager()
    while True:
        print('Enter your choice: ')
        print('1. Add information ')
        print('2. Get information ')
        print('3. Change infomation')
        print('4. Remove infomation')
        print('5. Exit ')
        choice = input('Choice: ')
        if choice == '1':
            manager.add_Info()
        elif choice == '2':
            manager.get_Info()
        elif choice == '3':
            manager.change_Info()
        elif choice == '4':
            manager.remove_Info()
        elif choice == '4':
            break
        else:
            print('Please enter valid choice!')

# Call the main function
if __name__ == "__main__":
    main()




