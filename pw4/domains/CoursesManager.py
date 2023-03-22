from domains.Course import Course
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
