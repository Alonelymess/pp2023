from domains.Student import Student
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
