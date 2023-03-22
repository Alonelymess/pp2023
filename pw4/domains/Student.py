
from domains.Utils import Utils
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
