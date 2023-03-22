from domains.Utils import Utils
import math
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
                if count > len(students_list) or count <= 0:
                    print('Invalid number of students!')
                    print('Currently there are', len(students_list), 'students in the list!')
                    continue
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
                student_id = int(input(f'Enter student {i+1} ID learn this course: '))
                for j in students_list:
                    if student_id == j.get_Id():
                        found = j

            mark = math.floor(float(input('Enter mark of this student: ')))
            while mark < 0 or mark > 20:
                mark = int(input('Please enter valid mark of this student: '))
            self.__students_learnt.append((found, mark))           

    def get_Students_learnt(self):
        return self.__students_learnt

    def show_Course(self):
        print(f'    Name: {self.get_Name()}    ID: {self.get_Id()}')
